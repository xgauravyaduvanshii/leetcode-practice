// LeetCode 3915. Maximum Sum of Alternating Subsequence With Distance at Least K — Hard
// https://leetcode.com/problems/maximum-sum-of-alternating-subsequence-with-distance-at-least-k/
// Submission 2203396889 — Accepted, JavaScript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxAlternatingSum = function(nums, k) {
    // My thinking: up[i] is the best score of a valid
    // subsequence ending at i whose last step goes up
    // (or a single element, which has no last step yet),
    // and down[i] the same with the last step going
    // down. A length-1 subsequence can be extended in
    // either direction, so up[i] is nums[i] plus the
    // best down[j] over eligible j with nums[j] <
    // nums[i], and down[i] is nums[i] plus the best
    // up[j] over eligible j with nums[j] > nums[i];
    // either term is 0 when no such j exists, which
    // just starts a fresh length-1 subsequence at i.
    // An index j becomes eligible once i - j >= k, so
    // I insert j = i - k as i advances. Both "best
    // over smaller values" and "best over larger
    // values" are prefix maxima over the value axis
    // (the second one on a reversed index), which two
    // Fenwick trees answer in O(log V) each. The
    // answer is the best up[i] or down[i].
    const n = nums.length;
    const vmax = Math.max(...nums);
    const bitLo = new Array(vmax + 2).fill(0); // down[j] at value nums[j]
    const bitHi = new Array(vmax + 2).fill(0); // up[j] at reversed value
    const bitUpdate = (bit, i, v) => {
        while (i <= vmax) {
            if (v > bit[i]) bit[i] = v;
            i += i & -i;
        }
    };
    const bitQuery = (bit, i) => {
        let r = 0;
        while (i > 0) {
            if (bit[i] > r) r = bit[i];
            i -= i & -i;
        }
        return r;
    };
    const up = new Array(n).fill(0);
    const down = new Array(n).fill(0);
    let ans = 0;
    for (let i = 0; i < n; i++) {
        const x = nums[i];
        if (i - k >= 0) {
            const j = i - k;
            bitUpdate(bitLo, nums[j], down[j]);
            bitUpdate(bitHi, vmax - nums[j] + 1, up[j]);
        }
        up[i] = x + bitQuery(bitLo, x - 1);
        down[i] = x + bitQuery(bitHi, vmax - x);
        if (up[i] > ans) ans = up[i];
        if (down[i] > ans) ans = down[i];
    }
    return ans;
};
