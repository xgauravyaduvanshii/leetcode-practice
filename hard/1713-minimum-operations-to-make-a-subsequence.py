# LeetCode 1713. Minimum Operations to Make a Subsequence — Hard
# https://leetcode.com/problems/minimum-operations-to-make-a-subsequence/
# Submission 2201108333 — Accepted, Python3
#
# My thinking: I keep only the target values that also
# appear in the array, turn them into positions, and
# the longest increasing run of those positions is the
# longest subsequence I already have — everything else
# has to be inserted.

from bisect import bisect_left

class Solution:
    def minOperations(self, target: list[int], arr: list[int]) -> int:
        pos = {v: i for i, v in enumerate(target)}
        seq = [pos[v] for v in arr if v in pos]
        tails = []
        for v in seq:
            i = bisect_left(tails, v)
            if i == len(tails):
                tails.append(v)
            else:
                tails[i] = v
        return len(target) - len(tails)
