# 4065. Rearrange Array by Removing Distinct Values (Easy)
# https://leetcode.com/problems/rearrange-array-by-removing-distinct-values/
# Submission 2200102040 — Accepted, Python3
from collections import Counter


class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        # My thinking: each round takes one copy of
        # every value that is still left, smallest
        # first. A value with three copies therefore
        # shows up once in each of the first three
        # rounds.
        counts = Counter(nums)
        ans = []
        for _ in range(max(counts.values())):
            for v in sorted(counts):
                if counts[v] > 0:
                    ans.append(v)
                    counts[v] -= 1
        return ans
