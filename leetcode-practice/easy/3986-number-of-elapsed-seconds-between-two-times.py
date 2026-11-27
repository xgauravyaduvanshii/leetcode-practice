# 3986. Number of Elapsed Seconds Between Two Times (Easy)
# https://leetcode.com/problems/number-of-elapsed-seconds-between-two-times/
# Submission 2200093391 — Accepted, Python3
class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        # My thinking: I turn each clock reading into
        # its total seconds since midnight, then take
        # the difference.
        def to_seconds(t: str) -> int:
            h, m, s = (int(part) for part in t.split(":"))
            return h * 3600 + m * 60 + s

        return to_seconds(endTime) - to_seconds(startTime)
