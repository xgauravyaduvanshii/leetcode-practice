# LeetCode 2437. Number of Valid Clock Times — Easy
# https://leetcode.com/problems/number-of-valid-clock-times/
# Submission 2197785285 — Accepted, Python3
#
# My thinking: I count how many hour values from 0 to
# 23 fit the hour pattern, and how many minute
# values from 0 to 59 fit the minute pattern. Any
# valid hour can pair with any valid minute, so I
# multiply the two counts.

class Solution:
    def countTime(self, time: str) -> int:
        h = time[:2]
        m = time[3:]
        hours = 0
        for hh in range(24):
            if (h[0] == '?' or h[0] == str(hh // 10)) and (h[1] == '?' or h[1] == str(hh % 10)):
                hours += 1
        minutes = 0
        for mm in range(60):
            if (m[0] == '?' or m[0] == str(mm // 10)) and (m[1] == '?' or m[1] == str(mm % 10)):
                minutes += 1
        return hours * minutes
