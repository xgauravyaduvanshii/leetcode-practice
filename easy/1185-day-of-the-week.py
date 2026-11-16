# LeetCode 1185. Day of the Week — Easy
# https://leetcode.com/problems/day-of-the-week/
# Submission 2197561970 — Accepted, Python3
#
# My thinking: Python's datetime already knows the
# calendar — I build the date and ask it for the
# weekday name. No need to work out leap years or
# day counts by hand.

import datetime


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return datetime.date(year, month, day).strftime("%A")
