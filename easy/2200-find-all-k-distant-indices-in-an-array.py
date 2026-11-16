# LeetCode 2200. Find All K-Distant Indices in an Array — Easy
# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/
# Submission 2197617286 — Accepted, Python3
#
# My thinking: I collect the positions where the key
# appears. An index counts when it is within k of
# any of those positions.

class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        keys = [i for i, x in enumerate(nums) if x == key]
        return [j for j in range(len(nums)) if any(abs(j - i) <= k for i in keys)]
