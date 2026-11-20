# 1856. Maximum Subarray Min-Product (Medium)
# https://leetcode.com/problems/maximum-subarray-min-product/
# Submission 2199950614 — Accepted, Python3
from typing import List


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        # My thinking: take every position as the minimum
        # of some subarray. A monotonic stack tells us how
        # far that minimum stretches on each side, and a
        # prefix sum gives the subarray total in O(1), so
        # the product for this minimum is quick to check.
        mod = 10 ** 9 + 7
        n = len(nums)
        prefix = [0] * (n + 1)
        for i, value in enumerate(nums):
            prefix[i + 1] = prefix[i] + value
        # left[i]: nearest index on the left with a value
        # strictly smaller than nums[i]; right[i]: nearest
        # index on the right with a value smaller or equal.
        left = [-1] * n
        right = [n] * n
        stack = []
        for i, value in enumerate(nums):
            while stack and nums[stack[-1]] >= value:
                right[stack.pop()] = i
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        best = 0
        for i, value in enumerate(nums):
            total = prefix[right[i]] - prefix[left[i] + 1]
            best = max(best, value * total)
        return best % mod
