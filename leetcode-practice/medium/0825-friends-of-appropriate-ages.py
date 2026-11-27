# LeetCode 825. Friends Of Appropriate Ages — Medium
# https://leetcode.com/problems/friends-of-appropriate-ages/
# Submission 2198948656 — Accepted, Python3
#
# My thinking: I count people by age and keep
# running totals, so for each age I know how many
# could receive a request — anyone older than
# half the age plus seven, up to the same age.
# Each sender counts those people minus
# themselves.

from typing import List


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        counts = [0] * 121
        for age in ages:
            counts[age] += 1
        prefix = [0] * 122
        for age in range(1, 121):
            prefix[age + 1] = prefix[age] + counts[age]
        total = 0
        for age in range(15, 121):
            low = age // 2 + 7
            in_range = prefix[age + 1] - prefix[low + 1]
            total += counts[age] * max(0, in_range - 1)
        return total
