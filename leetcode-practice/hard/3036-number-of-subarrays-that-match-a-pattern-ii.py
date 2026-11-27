# LeetCode 3036. Number of Subarrays That Match a Pattern II — Hard
# https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-ii/
# Submission 2201907295 — Accepted, Python3
#
# My thinking: I turn the numbers into
# the signs of their steps (+1 up, 0
# flat, -1 down), which turns the
# pattern into a plain string to search
# for. Then I run KMP over the signs:
# the prefix function on the pattern
# tells me where to resume after every
# mismatch, so the whole scan is linear.

from typing import List


class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n, m = len(nums), len(pattern)
        diff = []
        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                diff.append(1)
            elif nums[i + 1] < nums[i]:
                diff.append(-1)
            else:
                diff.append(0)
        # Prefix function of the pattern.
        pi = [0] * m
        for i in range(1, m):
            j = pi[i - 1]
            while j > 0 and pattern[i] != pattern[j]:
                j = pi[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
            pi[i] = j
        ans = 0
        j = 0
        for x in diff:
            while j > 0 and x != pattern[j]:
                j = pi[j - 1]
            if x == pattern[j]:
                j += 1
            if j == m:
                ans += 1
                j = pi[j - 1]
        return ans
