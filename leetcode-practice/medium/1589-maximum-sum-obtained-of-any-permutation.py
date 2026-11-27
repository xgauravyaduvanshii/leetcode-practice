# LeetCode 1589. Maximum Sum Obtained of Any Permutation — Medium
# https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/
# Submission 2199885776 — Accepted, Python3
#
# My thinking: an index covered by more
# requests deserves a bigger number. I count
# how many requests cover each index with a
# difference array, then pair the biggest
# counts with the biggest numbers.

from typing import List


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)
        diff = [0] * (n + 1)
        for start, end in requests:
            diff[start] += 1
            diff[end + 1] -= 1
        counts = []
        running = 0
        for i in range(n):
            running += diff[i]
            counts.append(running)
        counts.sort(reverse=True)
        nums.sort(reverse=True)
        return sum(count * value for count, value in zip(counts, nums)) % mod
