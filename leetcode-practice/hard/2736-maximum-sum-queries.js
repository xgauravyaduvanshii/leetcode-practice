// LeetCode 2736. Maximum Sum Queries — Hard
// https://leetcode.com/problems/maximum-sum-queries/
// Submission 2201878721 — Accepted, JavaScript
//
// My thinking: a query only cares
// about points whose first number
// clears its bar, so I sweep the bar
// downward, dropping each point into a
// tree keyed by its second number the
// moment it qualifies — and the tree
// always knows the best sum waiting at
// or above any second number.

function maximumSumQueries(nums1, nums2, queries) {
  const n = nums1.length;
  const points = nums1.map((a, i) => [a, nums2[i], a + nums2[i]]).sort((x, y) => y[0] - x[0]);
  const order = queries.map((_, i) => i).sort((i, j) => queries[j][0] - queries[i][0]);
  const vals = [...new Set(nums2)].sort((a, b) => a - b);
  const size = vals.length;
  // Fenwick tree for suffix maximum, indexed from the top down
  const bit = new Array(size + 1).fill(-1);
  function bitUpdate(i, v) {
    i += 1;
    while (i <= size) {
      if (v > bit[i]) bit[i] = v;
      i += i & -i;
    }
  }
  function bitQuery(i) {
    i += 1;
    let best = -1;
    while (i > 0) {
      if (bit[i] > best) best = bit[i];
      i -= i & -i;
    }
    return best;
  }
  function lowerBound(arr, target) {
    let lo = 0, hi = arr.length;
    while (lo < hi) {
      const mid = (lo + hi) >> 1;
      if (arr[mid] < target) lo = mid + 1;
      else hi = mid;
    }
    return lo;
  }
  const ans = new Array(queries.length).fill(-1);
  let p = 0;
  for (const qi of order) {
    const [x, y] = queries[qi];
    while (p < n && points[p][0] >= x) {
      const [, b, s] = points[p];
      const idx = size - 1 - lowerBound(vals, b);
      bitUpdate(idx, s);
      p++;
    }
    const cnt = size - lowerBound(vals, y);
    if (cnt > 0) ans[qi] = bitQuery(cnt - 1);
  }
  return ans;
}
