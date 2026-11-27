# LeetCode 2358. Maximum Number of Groups Entering a Competition — Medium
# https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/
# Submission 2204736676 — Accepted, Python3
#
# My thinking: only the count of students matters, not their grades — I
# can always arrange the groups so the sums increase as long as each
# group is bigger than the last. So I take the largest k with
# 1+2+...+k <= n, building it greedily one group at a time.
class Solution:
    def maximumGroups(self, grades: list[int]) -> int:
        n = len(grades)
        k = 0
        total = 0
        while total + k + 1 <= n:
            k += 1
            total += k
        return k
