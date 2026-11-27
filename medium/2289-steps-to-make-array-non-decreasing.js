// LeetCode 2289. Steps to Make Array Non-decreasing — Medium
// https://leetcode.com/problems/steps-to-make-array-non-decreasing/
// Submission 2204648673 — Accepted, JavaScript
//
// My thinking: same idea as the Python version — a stack of [value,
// steps] pairs for the elements still standing; each new x pops every
// stack top <= x, needs one more step than the worst of them, and needs
// 0 steps when nothing blocks it. The answer is the largest step count.
/**
 * @param {number[]} nums
 * @return {number}
 */
var totalSteps = function(nums) {
    const stack = [];
    let ans = 0;
    for (const x of nums) {
        let cur = 1;
        while (stack.length > 0 && stack[stack.length - 1][0] <= x) {
            cur = Math.max(cur, stack[stack.length - 1][1] + 1);
            stack.pop();
        }
        if (stack.length === 0) cur = 0;
        ans = Math.max(ans, cur);
        stack.push([x, cur]);
    }
    return ans;
};
