# LeetCode 881. Boats to Save People — Medium
# https://leetcode.com/problems/boats-to-save-people/
# Submission 2198961976 — Accepted, Python3
#
# My thinking: I pair the heaviest person with
# the lightest one whenever they fit together —
# the heaviest can only ever share with the
# lightest, so that pairing wastes nothing.

from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        left, right = 0, len(people) - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            boats += 1
        return boats
