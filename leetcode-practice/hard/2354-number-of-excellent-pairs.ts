// LeetCode 2354. Number of Excellent Pairs — Hard
// https://leetcode.com/problems/number-of-excellent-pairs/
// Submission 2201696787 — Accepted, TypeScript
//
// My thinking: the bits of an OR plus the
// bits of an AND are just the bits of both
// numbers together — so a pair is excellent
// when the two popcounts add up to k, and
// I count ordered pairs by popcount.

function countExcellentPairs(nums: number[], k: number): number {
  const freq = new Map<number, number>();
  for (const x of new Set(nums)) {
    let c = 0;
    let v = x;
    while (v > 0) {
      c += v & 1;
      v >>= 1;
    }
    freq.set(c, (freq.get(c) ?? 0) + 1);
  }
  let ans = 0;
  for (const [a, fa] of freq) {
    for (const [b, fb] of freq) {
      if (a + b >= k) ans += fa * fb;
    }
  }
  return ans;
}
