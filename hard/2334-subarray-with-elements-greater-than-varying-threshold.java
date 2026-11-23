// LeetCode 2334. Subarray With Elements Greater Than Varying Threshold — Hard
// https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold/
// Submission 2201686398 — Accepted, Java
//
// My thinking: the smallest number in a
// stretch decides what that stretch can
// be — I give each number the widest
// stretch where it stays the smallest and
// keep the widest one that clears the bar.

import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int validSubarraySize(int[] nums, int threshold) {
        int n = nums.length;
        int[] left = new int[n];
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && nums[stack.peek()] >= nums[i]) stack.pop();
            left[i] = stack.isEmpty() ? -1 : stack.peek();
            stack.push(i);
        }
        int[] right = new int[n];
        stack.clear();
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.isEmpty() && nums[stack.peek()] > nums[i]) stack.pop();
            right[i] = stack.isEmpty() ? n : stack.peek();
            stack.push(i);
        }
        int ans = -1;
        for (int i = 0; i < n; i++) {
            int length = right[i] - left[i] - 1;
            if ((long) length * nums[i] > threshold && length > ans) {
                ans = length;
            }
        }
        return ans;
    }
}
