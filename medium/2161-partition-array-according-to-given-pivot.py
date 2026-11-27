# LeetCode 2161. Partition Array According to Given Pivot — Medium
# https://leetcode.com/problems/partition-array-according-to-given-pivot/
# Submission 2204477894 — Accepted, Python3
#
# My thinking: the relative order inside each group must stay the same,
# so I do one stable pass that collects the elements smaller than the
# pivot, one that collects the equal ones, and one for the greater ones,
# then concatenate the three groups in that order.
class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        less = [x for x in nums if x < pivot]
        equal = [x for x in nums if x == pivot]
        greater = [x for x in nums if x > pivot]
        return less + equal + greater
