// LeetCode 2561. Rearranging Fruits — Hard
// https://leetcode.com/problems/rearranging-fruits/
// Submission 2201821815 — Accepted, JavaScript
//
// My thinking: a fruit can only be
// balanced if it appears an even number
// of times overall, so I gather what
// each basket has too much of, pair the
// cheapest spares together, and pay the
// smaller of a straight swap or two
// trips through the cheapest fruit of
// all.

/**
 * @param {number[]} basket1
 * @param {number[]} basket2
 * @return {number}
 */
var minCost = function(basket1, basket2) {
  const c1 = new Map();
  const c2 = new Map();
  for (const v of basket1) c1.set(v, (c1.get(v) || 0) + 1);
  for (const v of basket2) c2.set(v, (c2.get(v) || 0) + 1);
  const total = new Map();
  for (const [v, c] of c1) total.set(v, (total.get(v) || 0) + c);
  for (const [v, c] of c2) total.set(v, (total.get(v) || 0) + c);
  for (const t of total.values()) {
    if (t % 2 === 1) return -1;
  }
  const swap1 = [];
  const swap2 = [];
  for (const [v, t] of total) {
    const half = t / 2;
    const a = c1.get(v) || 0;
    const b = c2.get(v) || 0;
    if (a > half) for (let i = 0; i < a - half; i++) swap1.push(v);
    if (b > half) for (let i = 0; i < b - half; i++) swap2.push(v);
  }
  swap1.sort((x, y) => x - y);
  swap2.sort((x, y) => x - y);
  const cheapest = Math.min(...total.keys());
  let ans = 0;
  for (let i = 0; i < swap1.length; i++) {
    ans += Math.min(Math.min(swap1[i], swap2[i]), 2 * cheapest);
  }
  return ans;
};
