# LeetCode 2446. Determine if Two Events Have Conflict — Easy
# https://leetcode.com/problems/determine-if-two-events-have-conflict/
# Submission 2197786301 — Accepted, Python3
#
# My thinking: two events conflict when they overlap
# — the first starts before the second ends, and the
# second starts before the first ends.

class Solution:
    def haveConflict(self, event1: list[str], event2: list[str]) -> bool:
        return event1[0] <= event2[1] and event2[0] <= event1[1]
