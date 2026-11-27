# LeetCode 1154. Day of the Year — Easy
# https://leetcode.com/problems/day-of-the-year/
# Submission 2197559624 — Accepted, Python3
#
# My thinking: I split the date into year, month and
# day. February gets 29 days in a leap year (every
# 4 years, except centuries, unless divisible by
# 400). Then the day of the year is just the days
# of all the full months before this one, plus the
# day itself.

class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split("-"))
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        leap = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
        if leap:
            days[1] = 29
        return sum(days[:month - 1]) + day
