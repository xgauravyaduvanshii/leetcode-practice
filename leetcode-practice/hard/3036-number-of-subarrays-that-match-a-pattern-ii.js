// LeetCode 3036. Number of Subarrays That Match a Pattern II — Hard
// https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-ii/
// Submission 2201908004 — Accepted, JavaScript
//
// My thinking: I turn the numbers into
// the signs of their steps (+1 up, 0
// flat, -1 down), which turns the
// pattern into a plain string to search
// for. Then I run KMP over the signs:
// the prefix function on the pattern
// tells me where to resume after every
// mismatch, so the whole scan is linear.

/**
 * @param {number[]} nums
 * @param {number[]} pattern
 * @return {number}
 */
var countMatchingSubarrays = function(nums, pattern) {
    const n = nums.length, m = pattern.length;
    const diff = [];
    for (let i = 0; i < n - 1; i++) {
        diff.push(nums[i + 1] > nums[i] ? 1 : nums[i + 1] < nums[i] ? -1 : 0);
    }
    // Prefix function of the pattern.
    const pi = new Array(m).fill(0);
    for (let i = 1; i < m; i++) {
        let j = pi[i - 1];
        while (j > 0 && pattern[i] !== pattern[j]) j = pi[j - 1];
        if (pattern[i] === pattern[j]) j++;
        pi[i] = j;
    }
    let ans = 0, j = 0;
    for (const x of diff) {
        while (j > 0 && x !== pattern[j]) j = pi[j - 1];
        if (x === pattern[j]) j++;
        if (j === m) {
            ans++;
            j = pi[j - 1];
        }
    }
    return ans;
};
