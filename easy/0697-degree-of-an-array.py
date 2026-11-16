# LeetCode 697. Degree of an Array — Easy
# https://leetcode.com/problems/degree-of-an-array/
# Submission 2197516441 — Accepted, Python3
#
# My thinking: the degree is the biggest count of
# any number. For each number that appears that
# many times, the shortest subarray containing all
# of them runs from its first appearance to its
# last. I take the shortest of those.

class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        first = {}
        last = {}
        counts = {}
        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i
            counts[num] = counts.get(num, 0) + 1
        degree = max(counts.values())
        return min(last[num] - first[num] + 1 for num, c in counts.items() if c == degree)
