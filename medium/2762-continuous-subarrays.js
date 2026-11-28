// LeetCode 2762. Continuous Subarrays — Medium
// https://leetcode.com/problems/continuous-subarrays/
// Submission 2205247737 — Accepted, JavaScript
//
// My thinking: same idea as the Python version — a sliding
// window with two monotone deques for the current max and
// min; shrink from the left while the spread exceeds 2, and
// count (right - left + 1) subarrays ending at each right end.
/**
 * @param {number[]} nums
 * @return {number}
 */
var continuousSubarrays = function(nums) {
    const maxq = [], minq = [];
    let maxh = 0, minh = 0; // front indices into the deques
    let ans = 0, left = 0;
    for (let right = 0; right < nums.length; right++) {
        const v = nums[right];
        while (maxq.length > maxh && nums[maxq[maxq.length - 1]] <= v) maxq.pop();
        maxq.push(right);
        while (minq.length > minh && nums[minq[minq.length - 1]] >= v) minq.pop();
        minq.push(right);
        while (nums[maxq[maxh]] - nums[minq[minh]] > 2) {
            if (maxq[maxh] === left) maxh++;
            if (minq[minh] === left) minh++;
            left++;
        }
        ans += right - left + 1;
    }
    return ans;
};
