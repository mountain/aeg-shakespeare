// Phase 5 standalone C++ semantic benchmark for the Lonely Runner two-slot prune.
//
// This deliberately mirrors the relevant upstream find_cover semantics without
// depending on the upstream source tree.  It is used to separate the question
// "does the certificate survive C++/bitset cost?" from the later question
// "does a minimal patch improve the actual upstream binary?".
//
// Build from the repository root, for example:
//
//   g++ -O3 -std=c++23 -march=native \
//       sonnet/lonely-runner/cpp/phase5_two_slot_bench.cpp \
//       -o /tmp/lr-phase5
//   /tmp/lr-phase5
//
// Deterministic node/leaf counts are documented in 05-bounded-transversal-prune.md.
// Timings are machine-dependent and are diagnostics only.

#include <algorithm>
#include <array>
#include <bitset>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <limits>
#include <utility>
#include <vector>

static constexpr int MAX = 512;
using Bits = std::bitset<MAX>;

struct Context
{
  int k, p, half;
  Bits universe;
  std::vector<Bits> cover;

  Context(int kk, int pp) : k(kk), p(pp), half(pp / 2), cover(half)
  {
    for (int pos = 0; pos < half; ++pos) universe.set(pos);

    for (int i = 0; i < half; ++i)
      for (int t = 1; t <= half; ++t)
      {
        const int pos = half - t;
        const int rem = static_cast<int>((1LL * t * (i + 1)) % p);
        if (rem * (k + 1) < p || (p - rem) * (k + 1) < p) cover[i].set(pos);
      }
  }
};

struct ChoiceState
{
  std::array<unsigned char, MAX> eliminated{};
  std::array<uint16_t, MAX> remaining{};

  ChoiceState() = default;

  explicit ChoiceState(const Context& c)
  {
    for (int i = 0; i < c.half; ++i)
      for (int pos = 0; pos < c.half; ++pos)
        if (c.cover[i].test(pos)) remaining[pos]++;
  }

  void eliminate(const Context& c, int i)
  {
    if (eliminated[i]) return;
    eliminated[i] = 1;
    for (int pos = 0; pos < c.half; ++pos)
      if (c.cover[i].test(pos)) remaining[pos]--;
  }

  int next_to_cover(const Context& c, const Bits& covered) const
  {
    int best_pos = -1;
    int best = std::numeric_limits<int>::max();
    for (int pos = 0; pos < c.half; ++pos)
      if (!covered.test(pos) && remaining[pos] < best)
      {
        best = remaining[pos];
        best_pos = pos;
      }
    return best_pos;
  }
};

struct Stats
{
  uint64_t nodes = 0;
  uint64_t upstream_prune = 0;
  uint64_t two_checks = 0;
  uint64_t two_prune = 0;
  uint64_t accepted = 0;
};

bool upstream_bound(
    const Context& c,
    const Bits& covered,
    const ChoiceState& choice,
    int depth,
    int& selected)
{
  selected = choice.next_to_cover(c, covered);

  if (selected != -1 && choice.remaining[selected] == 0) return true;
  if (depth < c.k - 4 || selected == -1) return false;

  Bits other = c.universe & ~covered;
  other.reset(selected);

  const int total = c.half - static_cast<int>(covered.count());
  int best_next = 0;
  int best = 0;

  for (int i = 0; i < c.half; ++i)
  {
    if (choice.eliminated[i]) continue;
    const int count = static_cast<int>((other & c.cover[i]).count());
    best = std::max(best, count);
    if (c.cover[i].test(selected)) best_next = std::max(best_next, count + 1);
  }

  const int slots = c.k - depth;
  return total > best_next + best * (slots - 1);
}

bool two_slot_feasible(
    const Context& c,
    const Bits& covered,
    const ChoiceState& choice,
    int selected)
{
  const Bits uncovered = c.universe & ~covered;
  if (uncovered.none()) return true;

  if (selected == -1) selected = choice.next_to_cover(c, covered);
  if (selected == -1 || choice.remaining[selected] == 0) return false;

  // Every successful pair contains some first speed covering the current MRV
  // time position.  For each such speed, ask whether one remaining available
  // speed can cover the residual bitset.  Repetition is allowed, matching the
  // upstream child semantics: the chosen speed is eliminated only for later
  // siblings after its child returns.
  for (int first = 0; first < c.half; ++first)
  {
    if (choice.eliminated[first] || !c.cover[first].test(selected)) continue;

    const Bits residual = uncovered & ~c.cover[first];
    if (residual.none()) return true;

    for (int second = 0; second < c.half; ++second)
    {
      if (choice.eliminated[second]) continue;
      if ((residual & ~c.cover[second]).none()) return true;
    }
  }

  return false;
}

void dfs(
    const Context& c,
    Bits covered,
    ChoiceState choice,
    int depth,
    bool enhanced,
    Stats& stats)
{
  stats.nodes++;

  if (depth == c.k)
  {
    if ((covered & c.universe) == c.universe) stats.accepted++;
    return;
  }

  int selected = -1;
  if (upstream_bound(c, covered, choice, depth, selected))
  {
    stats.upstream_prune++;
    return;
  }

  if (enhanced && c.k - depth == 2)
  {
    stats.two_checks++;
    if (!two_slot_feasible(c, covered, choice, selected))
    {
      stats.two_prune++;
      return;
    }
  }

  for (int i = 0; i < c.half; ++i)
  {
    if (choice.eliminated[i]) continue;
    if (selected == -1 || c.cover[i].test(selected))
    {
      dfs(c, covered | c.cover[i], choice, depth + 1, enhanced, stats);
      choice.eliminate(c, i);
    }
  }
}

Stats run_whole(int k, int p, bool enhanced)
{
  Context c(k, p);
  Stats stats;
  ChoiceState base(c);
  const Bits first = c.cover[0];
  const int next = base.next_to_cover(c, first);

  std::vector<int> candidates;
  for (int i = 0; i < c.half; ++i)
    if (next == -1 || c.cover[i].test(next)) candidates.push_back(i);

  ChoiceState choice = base;
  for (int i : candidates)
  {
    dfs(c, first | c.cover[i], choice, 2, enhanced, stats);
    choice.eliminate(c, i);
  }
  return stats;
}

Stats run_worker(int k, int p, int worker, bool enhanced, int& second_speed)
{
  Context c(k, p);
  Stats stats;
  ChoiceState base(c);
  const Bits first = c.cover[0];
  const int next = base.next_to_cover(c, first);

  std::vector<int> candidates;
  for (int i = 0; i < c.half; ++i)
    if (next == -1 || c.cover[i].test(next)) candidates.push_back(i);

  ChoiceState choice = base;
  for (int i = 0; i < worker; ++i) choice.eliminate(c, candidates[i]);

  const int selected = candidates.at(worker);
  second_speed = selected + 1;
  dfs(c, first | c.cover[selected], choice, 2, enhanced, stats);
  return stats;
}

template <class F> auto timed(F&& f)
{
  const auto start = std::chrono::steady_clock::now();
  auto value = f();
  const auto finish = std::chrono::steady_clock::now();
  const double milliseconds =
      std::chrono::duration<double, std::milli>(finish - start).count();
  return std::pair{value, milliseconds};
}

void print_stats(const char* tag, const Stats& stats, double milliseconds)
{
  std::cout << tag << " nodes=" << stats.nodes << " accepted=" << stats.accepted
            << " upstream_prune=" << stats.upstream_prune
            << " two_prune=" << stats.two_prune
            << " checks=" << stats.two_checks
            << " time_ms=" << milliseconds << '\n';
}

int main()
{
  for (const auto [k, p] : std::vector<std::pair<int, int>>{{8, 79}, {9, 89}})
  {
    const auto [baseline, baseline_ms] = timed([&] { return run_whole(k, p, false); });
    const auto [enhanced, enhanced_ms] = timed([&] { return run_whole(k, p, true); });

    std::cout << "CASE k=" << k << " p=" << p << '\n';
    print_stats("baseline", baseline, baseline_ms);
    print_stats("two-slot", enhanced, enhanced_ms);
  }

  std::cout << "CASE k=10 p=127 first five workers\n";
  for (int worker = 0; worker < 5; ++worker)
  {
    int baseline_second = 0;
    int enhanced_second = 0;
    const auto [baseline, baseline_ms] = timed([&] {
      return run_worker(10, 127, worker, false, baseline_second);
    });
    const auto [enhanced, enhanced_ms] = timed([&] {
      return run_worker(10, 127, worker, true, enhanced_second);
    });

    if (baseline_second != enhanced_second || baseline.accepted != enhanced.accepted)
    {
      std::cerr << "semantic mismatch in worker " << worker << '\n';
      return 1;
    }

    std::cout << "worker second=" << baseline_second << '\n';
    print_stats("baseline", baseline, baseline_ms);
    print_stats("two-slot", enhanced, enhanced_ms);
  }
}
