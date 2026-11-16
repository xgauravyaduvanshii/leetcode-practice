# LeetCode 1331. Rank Transform of an Array — Easy
# https://leetcode.com/problems/rank-transform-of-an-array/
# Submission 2197571039 — Accepted, Python3
#
# My thinking: I sort the distinct values and give
# each one its position (starting from 1) as its
# rank. Equal values share the same rank. Then I
# just look up the rank of each number in the
# original order.

class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        ranks = {v: i + 1 for i, v in enumerate(sorted(set(arr)))}
        return [ranks[v] for v in arr]
