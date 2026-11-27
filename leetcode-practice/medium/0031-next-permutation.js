// LeetCode 31. Next Permutation — Medium
// https://leetcode.com/problems/next-permutation/
// Submission 2203816041 — Accepted, JavaScript

// My thinking: I scan from the right for the first position where the
// number rises — everything after it is falling, so it is the largest
// arrangement of that tail. I swap that position with the smallest
// number after it that is still bigger than it, then reverse the tail
// to make it the smallest possible. If nothing rises, the whole array
// is already the largest, so reversing it gives the smallest.
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var nextPermutation = function(nums) {
    const n = nums.length;
    let pivot = n - 2;
    while (pivot >= 0 && nums[pivot] >= nums[pivot + 1]) pivot--;
    if (pivot >= 0) {
        let swap = n - 1;
        while (nums[swap] <= nums[pivot]) swap--;
        [nums[pivot], nums[swap]] = [nums[swap], nums[pivot]];
    }
    let left = pivot + 1, right = n - 1;
    while (left < right) {
        [nums[left], nums[right]] = [nums[right], nums[left]];
        left++;
        right--;
    }
};
