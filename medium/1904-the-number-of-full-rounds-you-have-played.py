# LeetCode 1904. The Number of Full Rounds You Have Played — Medium
# https://leetcode.com/problems/the-number-of-full-rounds-you-have-played/
# Submission 2201204114 — Accepted, Python3
#
# My thinking: I round the login time up to the
# next quarter hour and the logout time down to
# the previous one — every fifteen minutes left
# between them is one full round.

class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        def minutes(t):
            return int(t[:2]) * 60 + int(t[3:])

        start, end = minutes(loginTime), minutes(logoutTime)
        if end < start:
            end += 24 * 60
        start = (start + 14) // 15 * 15
        end = end // 15 * 15
        return max(0, (end - start) // 15)
