// Harness for benchmarking the *actual pinned upstream* find_cover.h source.
//
// This file is compiled twice by the dedicated GitHub Actions workflows:
// once against an untouched checkout of vzsky/13-lonely-runners and once against
// the same checkout after applying phase5-two-slot-find-cover.patch.
//
// Whole-search usage:
//   ./harness dump 79
//   ./harness bench 127 15 3
//
// Top-level-worker usage:
//   ./harness worker-info 199
//   ./harness worker-dump 199 0 > worker.txt 2> worker.meta
//   ./harness worker-lift-sample 199 0 2000
//
// `worker-dump` times only the upstream Dfs worker computation.  Timing metadata
// goes to stderr while the complete sorted canonical solution set goes to stdout,
// so baseline/patched stdout can be compared byte-for-byte from a single run.

#include <algorithm>
#include <array>
#include <chrono>
#include <iomanip>
#include <iostream>
#include <stdexcept>
#include <streambuf>
#include <string>
#include <utility>
#include <vector>

#include "find_cover.h"
#include "lift.h"

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

template <int K> auto sorted_rows(const SetOfSpeedSets<K>& solutions)
{
  std::vector<std::array<int, K>> rows;
  rows.reserve(solutions.size());

  for (const auto& solution : solutions)
  {
    std::array<int, K> row{};
    std::copy(solution.begin(), solution.end(), row.begin());
    rows.push_back(row);
  }

  std::sort(rows.begin(), rows.end());
  return rows;
}

template <int K> void print_rows(const std::vector<std::array<int, K>>& rows)
{
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

template <int P, int K> void dump_case()
{
  auto solutions = solve_silent<P, K>();
  auto rows = sorted_rows<K>(solutions);

  std::cout << "P=" << P << " K=" << K << " N=" << rows.size() << '\n';
  print_rows<K>(rows);
}

template <int P, int K> void bench_case(int repeats, int warmups)
{
  // Warm the static context and allocator/thread machinery before recording.
  for (int i = 0; i < warmups; ++i) (void)solve_silent<P, K>();

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
            << " warmups=" << warmups
            << " median_ms=" << median
            << " mean_ms=" << total / repeats
            << " min_ms=" << minimum << '\n';
}

template <int P, int K> struct WorkerSetup
{
  using Dfs = find_cover::Dfs<P, K>;
  using CoveredBitset = typename Dfs::CoveredBitset;
  using AvailableChoice = typename Dfs::State::AvailableChoice;

  AvailableChoice base_choice{};
  CoveredBitset first_covered{};
  SpeedSet<K> first_elems{};
  std::vector<int> coord2_candidates;
  std::vector<AvailableChoice> choices;

  WorkerSetup()
  {
    first_elems.insert(1);
    first_covered |= find_cover::context<P, K>.cover(0);

    const int next_to_cover = base_choice.get_next_to_cover(first_covered);
    for (int i = 0; i < P / 2; ++i)
      if (next_to_cover == -1 || find_cover::context<P, K>.cover(i)[next_to_cover])
        coord2_candidates.push_back(i);

    choices.resize(coord2_candidates.size() + 1);
    choices[0] = base_choice;
    for (std::size_t idx = 0; idx < coord2_candidates.size(); ++idx)
    {
      choices[idx + 1] = choices[idx];
      choices[idx + 1].eliminate(coord2_candidates[idx]);
    }
  }
};

template <int P, int K> void worker_info()
{
  WorkerSetup<P, K> setup;
  std::cout << "P=" << P << " K=" << K
            << " workers=" << setup.coord2_candidates.size() << " second_speeds=";
  for (std::size_t idx = 0; idx < setup.coord2_candidates.size(); ++idx)
  {
    if (idx) std::cout << ',';
    std::cout << setup.coord2_candidates[idx] + 1;
  }
  std::cout << '\n';
}

template <int P, int K> void worker_dump(std::size_t worker_index)
{
  using Dfs = find_cover::Dfs<P, K>;

  WorkerSetup<P, K> setup;
  if (worker_index >= setup.coord2_candidates.size())
    throw std::out_of_range("worker index out of range");

  const int choice = setup.coord2_candidates[worker_index];
  SpeedSet<K> local_elems = setup.first_elems;
  local_elems.insert(choice + 1);

  Dfs dfs(typename Dfs::State{
      setup.first_covered | find_cover::context<P, K>.cover(choice),
      local_elems,
      setup.choices[worker_index],
  });

  const auto start = std::chrono::steady_clock::now();
  dfs.run();
  const auto finish = std::chrono::steady_clock::now();
  const double milliseconds =
      std::chrono::duration<double, std::milli>(finish - start).count();

  auto rows = sorted_rows<K>(dfs.solutions);

  // Keep timing/provenance out of stdout so exact set files can be compared.
  std::cerr << std::fixed << std::setprecision(3)
            << "WORKER P=" << P << " K=" << K
            << " index=" << worker_index
            << " second=" << choice + 1
            << " N=" << rows.size()
            << " solve_ms=" << milliseconds << '\n';

  std::cout << "P=" << P << " K=" << K
            << " worker=" << worker_index
            << " second=" << choice + 1
            << " N=" << rows.size() << '\n';
  print_rows<K>(rows);
}

template <int P, int K>
void worker_lift_sample(std::size_t worker_index, std::size_t sample_limit)
{
  using Dfs = find_cover::Dfs<P, K>;

  WorkerSetup<P, K> setup;
  if (worker_index >= setup.coord2_candidates.size())
    throw std::out_of_range("worker index out of range");
  if (sample_limit == 0) throw std::invalid_argument("sample limit must be positive");

  const int choice = setup.coord2_candidates[worker_index];
  SpeedSet<K> local_elems = setup.first_elems;
  local_elems.insert(choice + 1);
  Dfs dfs(typename Dfs::State{
      setup.first_covered | find_cover::context<P, K>.cover(choice),
      local_elems,
      setup.choices[worker_index],
  });

  const auto solve_start = std::chrono::steady_clock::now();
  dfs.run();
  const auto solve_finish = std::chrono::steady_clock::now();

  // The upstream carrier is an unordered_set.  Sort before sampling so the
  // declared prefix is semantic and reproducible across hash-table layouts.
  const auto rows = sorted_rows<K>(dfs.solutions);
  const std::size_t sampled = std::min(sample_limit, rows.size());
  const auto measure = [&](auto row_index)
  {
    std::size_t surviving_seeds = 0;
    std::size_t lifted_classes = 0;
    for (std::size_t sample = 0; sample < sampled; ++sample)
    {
      const SpeedSet<K> seed(rows[row_index(sample)]);
      const auto lifts = lift::lift<2, 1, P, K>(seed);
      if (!lifts.empty()) ++surviving_seeds;
      lifted_classes += lifts.size();
    }
    return std::pair{surviving_seeds, lifted_classes};
  };

  const auto lift_start = std::chrono::steady_clock::now();
  const auto prefix = measure([](std::size_t sample) { return sample; });
  const auto stratified = measure(
      [&](std::size_t sample) { return sample * rows.size() / sampled; });
  const auto lift_finish = std::chrono::steady_clock::now();

  const double solve_ms =
      std::chrono::duration<double, std::milli>(solve_finish - solve_start).count();
  const double lift_ms =
      std::chrono::duration<double, std::milli>(lift_finish - lift_start).count();
  std::cout << std::fixed << std::setprecision(3)
            << "P=" << P << " K=" << K
            << " worker=" << worker_index
            << " second=" << choice + 1
            << " solutions=" << rows.size()
            << " sampled=" << sampled
            << " prefix_order=lexicographic"
            << " prefix_surviving_seeds=" << prefix.first
            << " prefix_lifted_classes=" << prefix.second
            << " stratified_order=equidistant_lexicographic"
            << " stratified_surviving_seeds=" << stratified.first
            << " stratified_lifted_classes=" << stratified.second
            << " solve_ms=" << solve_ms
            << " lift_ms=" << lift_ms << '\n';
}

template <class F> void dispatch_case(int p, F&& f)
{
  switch (p)
  {
    case 79: f.template operator()<79, 8>(); break;
    case 89: f.template operator()<89, 9>(); break;
    case 127: f.template operator()<127, 10>(); break;
    case 131: f.template operator()<131, 11>(); break;
    case 139: f.template operator()<139, 12>(); break;
    case 199: f.template operator()<199, 13>(); break;
    default: throw std::invalid_argument("unsupported prime");
  }
}
} // namespace

int main(int argc, char** argv)
{
  if (argc < 3)
  {
    std::cerr
        << "usage: harness dump P | harness bench P REPEATS [WARMUPS] | "
           "harness worker-info P | harness worker-dump P INDEX | "
           "harness worker-lift-sample P INDEX LIMIT\n";
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
    if (argc != 4 && argc != 5) return 2;
    const int repeats = std::stoi(argv[3]);
    const int warmups = argc == 5 ? std::stoi(argv[4]) : 3;
    if (repeats <= 0 || warmups < 0) return 2;
    dispatch_case(p, [repeats, warmups]<int P, int K> {
      bench_case<P, K>(repeats, warmups);
    });
    return 0;
  }

  if (mode == "worker-info")
  {
    if (argc != 3) return 2;
    dispatch_case(p, []<int P, int K> { worker_info<P, K>(); });
    return 0;
  }

  if (mode == "worker-dump")
  {
    if (argc != 4) return 2;
    const auto worker_index = static_cast<std::size_t>(std::stoull(argv[3]));
    dispatch_case(p, [worker_index]<int P, int K> {
      worker_dump<P, K>(worker_index);
    });
    return 0;
  }

  if (mode == "worker-lift-sample")
  {
    if (argc != 5) return 2;
    const auto worker_index = static_cast<std::size_t>(std::stoull(argv[3]));
    const auto sample_limit = static_cast<std::size_t>(std::stoull(argv[4]));
    dispatch_case(p, [worker_index, sample_limit]<int P, int K> {
      worker_lift_sample<P, K>(worker_index, sample_limit);
    });
    return 0;
  }

  return 2;
}
