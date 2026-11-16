# LeetCode 1360. Number of Days Between Two Dates — Easy
# https://leetcode.com/problems/number-of-days-between-two-dates/
# Submission 2197572797 — Accepted, Python3
#
# My thinking: I parse both dates into real date
# objects and subtract them — Python handles the
# leap years and month lengths. The absolute value
# of the difference in days is the answer.

import datetime


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        d1 = datetime.date.fromisoformat(date1)
        d2 = datetime.date.fromisoformat(date2)
        return abs((d1 - d2).days)
