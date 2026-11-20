# 3041. Maximize Consecutive Elements in an Array After Modification (Hard)
# https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/
# Submission 2199961288 — Accepted, Python3
from typing import List


class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        # My thinking: sort the numbers first, then keep a
        # table of the longest run ending at each value.
        # Every number can stay as it is, stretching the
        # run that ends one below it, or grow by one,
        # stretching the run that ends at itself. Both
        # choices are read from the table before this
        # number writes into it, so no number is ever
        # used twice.
        nums.sort()
        longest = {}
        best = 0
        for x in nums:
            stay = longest.get(x - 1, 0) + 1
            grow = longest.get(x, 0) + 1
            longest[x] = max(longest.get(x, 0), stay)
            longest[x + 1] = max(longest.get(x + 1, 0), grow)
            best = max(best, longest[x], longest[x + 1])
        return best
