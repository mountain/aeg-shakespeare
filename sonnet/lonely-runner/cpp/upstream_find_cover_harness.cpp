// Harness for benchmarking the *actual pinned upstream* find_cover.h source.
//
// This file is compiled twice by the dedicated GitHub Actions workflow:
// once against an untouched checkout of vzsky/13-lonely-runners and once against
// the same checkout after applying phase5-two-slot-find-cover.patch.
//
// Usage:
//   ./harness dump 79
//   ./harness bench 127 15
//
// Supported cases are the configured solved-parameter probes used by Sonnet 001:
//   (K,P) = (8,79), (9,89), (10,127).

#include <algorithm>
#include <array>
#include <chrono>
#include <iostream>
#include <stdexcept>
#include <streambuf>
#include <string>
#include <vector>

#include "find_cover.h"

namespace
{
struct NullBuffer : std::streambuf
{
  int overflow(int c) override { return c; }
};

template <int P, int K> auto solve_silent()
{
  NullBuffer null_buffer;
  auto* old = std::cout.rdbuf(&null_buffer);
  auto solutions = find_cover::find_all_covers_parallel<P, K>();
  std::cout.rdbuf(old);
  return solutions;
}

template <int P, int K> void dump_case()
{
  auto solutions = solve_silent<P, K>();
  std::vector<std::array<int, K>> rows;
  rows.reserve(solutions.size());

  for (const auto& solution : solutions)
  {
    std::array<int, K> row{};
    std::copy(solution.begin(), solution.end(), row.begin());
    rows.push_back(row);
  }

  std::sort(rows.begin(), rows.end());
  std::cout << "P=" << P << " K=" << K << " N=" << rows.size() << '\n';
  for (const auto& row : rows)
  {
    for (int i = 0; i < K; ++i)
    {
      if (i) std::cout << ',';
      std::cout << row[i];
    }
    std::cout << '\n';
  }
}

template <int P, int K> void bench_case(int repeats)
{
  // Warm the static context and allocator/thread machinery before recording.
  for (int i = 0; i < 3; ++i) (void)solve_silent<P, K>();

  std::vector<double> milliseconds;
  milliseconds.reserve(repeats);
  std::size_t expected_size = 0;

  for (int i = 0; i < repeats; ++i)
  {
    const auto start = std::chrono::steady_clock::now();
    auto solutions = solve_silent<P, K>();
    const auto finish = std::chrono::steady_clock::now();

    if (i == 0)
      expected_size = solutions.size();
    else if (solutions.size() != expected_size)
      throw std::runtime_error("solution count changed between repeats");

    milliseconds.push_back(
        std::chrono::duration<double, std::milli>(finish - start).count());
  }

  std::sort(milliseconds.begin(), milliseconds.end());
  const double median = milliseconds[milliseconds.size() / 2];
  const double minimum = milliseconds.front();
  double total = 0.0;
  for (double value : milliseconds) total += value;

  std::cout << "P=" << P << " K=" << K << " N=" << expected_size
            << " repeats=" << repeats
            << " median_ms=" << median
            << " mean_ms=" << total / repeats
            << " min_ms=" << minimum << '\n';
}

template <class F> void dispatch_case(int p, F&& f)
{
  switch (p)
  {
    case 79: f.template operator()<79, 8>(); break;
    case 89: f.template operator()<89, 9>(); break;
    case 127: f.template operator()<127, 10>(); break;
    default: throw std::invalid_argument("unsupported prime");
  }
}
} // namespace

int main(int argc, char** argv)
{
  if (argc < 3)
  {
    std::cerr << "usage: harness dump P | harness bench P REPEATS\n";
    return 2;
  }

  const std::string mode = argv[1];
  const int p = std::stoi(argv[2]);

  if (mode == "dump")
  {
    dispatch_case(p, []<int P, int K> { dump_case<P, K>(); });
    return 0;
  }

  if (mode == "bench")
  {
    if (argc != 4) return 2;
    const int repeats = std::stoi(argv[3]);
    if (repeats <= 0) return 2;
    dispatch_case(p, [repeats]<int P, int K> { bench_case<P, K>(repeats); });
    return 0;
  }

  return 2;
}
