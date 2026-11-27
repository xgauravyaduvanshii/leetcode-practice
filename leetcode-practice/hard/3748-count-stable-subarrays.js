// LeetCode 3748. Count Stable Subarrays — Hard
// https://leetcode.com/problems/count-stable-subarrays/
// Submission 2203152546 — Accepted, JavaScript
/**
 * @param {number[]} nums
 * @param {number[][]} queries
 * @return {number[]}
 */
var countStableSubarrays = function(nums, queries) {
    // My thinking: a subarray is stable exactly when it is
    // non-decreasing, so every position i belongs to one
    // maximal non-decreasing run. Let L[i] be the start of
    // the run ending at i and f(i) = i - L[i] + 1 the number
    // of stable subarrays ending at i. For a query [l, r]
    // the runs are the key: inside the run that contains l,
    // a stable subarray ending at i can only start at or
    // after l, contributing i - l + 1; past that run every
    // run starts at or after l, so each i contributes the
    // full f(i). A prefix sum of f answers the second part
    // in O(1), and the first part is a triangular number,
    // so each query is O(1) after one linear pass.
    const n = nums.length;
    const start = new Array(n).fill(0);
    for (let i = 1; i < n; i++) {
        start[i] = nums[i] >= nums[i - 1] ? start[i - 1] : i;
    }
    const runEnd = new Array(n).fill(0);
    let j = 0;
    while (j < n) {
        let k = j;
        while (k + 1 < n && nums[k + 1] >= nums[k]) k++;
        for (let t = j; t <= k; t++) runEnd[t] = k;
        j = k + 1;
    }
    const pref = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) pref[i + 1] = pref[i] + (i - start[i] + 1);
    const ans = [];
    for (const [l, r] of queries) {
        const e = Math.min(r, runEnd[l]);
        const cnt = e - l + 1;
        const first = cnt * (cnt + 1) / 2;
        const second = pref[r + 1] - pref[e + 1];
        ans.push(first + second);
    }
    return ans;
};
