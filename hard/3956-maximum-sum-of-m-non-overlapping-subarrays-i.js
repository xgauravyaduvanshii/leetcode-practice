// LeetCode 3956. Maximum Sum of M Non-Overlapping Subarrays I — Hard
// https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-i/
// Submission 2203455888 — Accepted, JavaScript
/**
 * @param {number[]} nums
 * @param {number} m
 * @param {number} l
 * @param {number} r
 * @return {number}
 */
var maximumSum = function(nums, m, l, r) {
    // My thinking: dp[k][i] is the best sum using exactly k
    // subarrays inside the first i elements. Either the ith
    // element is unused (carry dp[k][i-1] forward) or a
    // subarray ends at i: its start j ranges over
    // [i-r, i-l], giving dp[k-1][j] + pref[i] - pref[j].
    // That is pref[i] plus the best of dp[k-1][j] - pref[j]
    // over a sliding window, which a monotone deque keeps in
    // O(1) amortised time — so each k costs one linear pass.
    // The answer is the best over k = 1..m, since at least
    // one subarray must be taken and extra ones may be
    // skipped when they would only lower the sum.
    const n = nums.length;
    const pref = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
    const NEG = -1e18;
    let dpPrev = new Array(n + 1).fill(0);
    let ans = NEG;
    for (let k = 1; k <= m; k++) {
        const dpCur = new Array(n + 1).fill(NEG);
        const dq = [];
        let head = 0;
        for (let i = 1; i <= n; i++) {
            const j = i - l;
            if (j >= 0 && dpPrev[j] > NEG / 2) {
                const val = dpPrev[j] - pref[j];
                while (dq.length > head && dpPrev[dq[dq.length - 1]] - pref[dq[dq.length - 1]] <= val) dq.pop();
                dq.push(j);
            }
            while (dq.length > head && dq[head] < i - r) head++;
            if (dq.length > head) {
                dpCur[i] = pref[i] + (dpPrev[dq[head]] - pref[dq[head]]);
            }
            if (dpCur[i - 1] > dpCur[i]) dpCur[i] = dpCur[i - 1];
        }
        if (dpCur[n] > ans) ans = dpCur[n];
        dpPrev = dpCur;
    }
    return ans;
};
