// LeetCode 2659. Make Array Empty — Hard
// https://leetcode.com/problems/make-array-empty/
// Submission 2201862338 — Accepted, JavaScript
//
// My thinking: the numbers leave in
// increasing order, so for each one I
// count how many are still standing
// between the front of the line and it
// — those all have to step aside first,
// and a Fenwick tree keeps the count
// honest as the line thins out.

/**
 * @param {number[]} nums
 * @return {number}
 */
var countOperationsToEmptyArray = function(nums) {
  const n = nums.length;
  const pos = new Map();
  nums.forEach((v, i) => pos.set(v, i));
  const bit = new Array(n + 1).fill(0);
  const bitAdd = (i, delta) => {
    i++;
    while (i <= n) {
      bit[i] += delta;
      i += i & -i;
    }
  };
  const bitSum = (i) => {
    if (i < 0) return 0;
    i++;
    let s = 0;
    while (i > 0) {
      s += bit[i];
      i -= i & -i;
    }
    return s;
  };
  for (let i = 0; i < n; i++) bitAdd(i, 1);
  let front = 0;
  let ops = 0;
  for (const v of [...nums].sort((a, b) => a - b)) {
    const p = pos.get(v);
    let before;
    if (p >= front) before = bitSum(p - 1) - bitSum(front - 1);
    else before = bitSum(n - 1) - bitSum(front - 1) + bitSum(p - 1);
    ops += before + 1;
    bitAdd(p, -1);
    if (bitSum(n - 1) === 0) break;
    if (bitSum(n - 1) - bitSum(p) > 0) {
      let lo = p + 1, hi = n - 1;
      while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (bitSum(mid) - bitSum(p) > 0) hi = mid;
        else lo = mid + 1;
      }
      front = lo;
    } else {
      let lo = 0, hi = n - 1;
      while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (bitSum(mid) > 0) hi = mid;
        else lo = mid + 1;
      }
      front = lo;
    }
  }
  return ops;
};
