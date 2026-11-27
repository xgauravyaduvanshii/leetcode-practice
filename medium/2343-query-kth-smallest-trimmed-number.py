# LeetCode 2343. Query Kth Smallest Trimmed Number — Medium
# https://leetcode.com/problems/query-kth-smallest-trimmed-number/
# Submission 2204716994 — Accepted, Python3
#
# My thinking: for each query I sort the indices by the trimmed suffix
# of their number, breaking ties by the smaller index (a stable sort on
# the pair (suffix, index)). The k-th smallest is the element at position
# k-1 of that order. Trimming is just a string slice from the right.
class Solution:
    def smallestTrimmedNumbers(self, nums: list[str], queries: list[list[int]]) -> list[int]:
        ans = []
        for k, trim in queries:
            idx = sorted(range(len(nums)), key=lambda i: (nums[i][-trim:], i))
            ans.append(idx[k - 1])
        return ans
