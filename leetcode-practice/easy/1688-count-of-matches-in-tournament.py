# LeetCode 1688. Count of Matches in Tournament — Easy
# https://leetcode.com/problems/count-of-matches-in-tournament/
# Submission 2197593731 — Accepted, Python3
#
# My thinking: every match knocks exactly one team
# out, and the tournament ends with one winner.
# So the number of matches is just n - 1, however
# the rounds are arranged.

class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n - 1
