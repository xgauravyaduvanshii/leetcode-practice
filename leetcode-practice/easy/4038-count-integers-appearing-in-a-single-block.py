# 4038. Count Integers Appearing in a Single Block (Easy)
# https://leetcode.com/problems/count-integers-appearing-in-a-single-block/
# Submission 2200099062 — Accepted, Python3
class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        # My thinking: a value is special when all its
        # copies sit together in one block — that is
        # when the gap from its first to its last
        # appearance holds exactly its copies, no more.
        first = {}
        last = {}
        counts = {}
        for i, x in enumerate(nums):
            if x not in first:
                first[x] = i
            last[x] = i
            counts[x] = counts.get(x, 0) + 1
        return sum(1 for x in counts if last[x] - first[x] + 1 == counts[x])
