# LeetCode 1385. Find the Distance Value Between Two Arrays — Easy
# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
# Submission 2197575040 — Accepted, Python3
#
# My thinking: for each number in arr1, I check it
# against every number in arr2 — it counts only if
# it is farther than d away from all of them. A
# simple double loop is enough here.

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = 0
        for x in arr1:
            if all(abs(x - y) > d for y in arr2):
                count += 1
        return count
