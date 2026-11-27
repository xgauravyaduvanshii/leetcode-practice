# LeetCode 907. Sum of Subarray Minimums — Medium
# https://leetcode.com/problems/sum-of-subarray-minimums/
# Submission 2198966333 — Accepted, Python3
#
# My thinking: each number is the minimum of
# exactly the subarrays that stretch from its
# previous smaller neighbour to its next smaller
# or equal one. I count those with a monotonic
# stack and add each number's share.

from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        stack = []
        total = 0
        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                j = stack.pop()
                left = j - (stack[-1] if stack else -1)
                right = i - j
                total += arr[j] * left * right
            stack.append(i)
        n = len(arr)
        while stack:
            j = stack.pop()
            left = j - (stack[-1] if stack else -1)
            right = n - j
            total += arr[j] * left * right
        return total % MOD
