# LeetCode 2848. Points That Intersect With Cars — Easy
# https://leetcode.com/problems/points-that-intersect-with-cars/
# Submission 2198421995 — Accepted, Python3
#
# My thinking: I mark every integer point covered
# by each car's range in a set, and the size of the
# set is the answer — a point covered by several
# cars is only counted once.

from typing import List


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered = set()
        for start, end in nums:
            for point in range(start, end + 1):
                covered.add(point)
        return len(covered)
