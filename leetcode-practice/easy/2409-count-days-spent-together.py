# LeetCode 2409. Count Days Spent Together — Easy
# https://leetcode.com/problems/count-days-spent-together/
# Submission 2197780377 — Accepted, Python3
#
# My thinking: I convert each month-day date into a
# day-of-year number. The days together are the
# overlap of the two ranges — from the later arrival
# to the earlier departure.

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def to_day(s):
            m, d = s.split('-')
            return sum(days[:int(m) - 1]) + int(d)

        start = max(to_day(arriveAlice), to_day(arriveBob))
        end = min(to_day(leaveAlice), to_day(leaveBob))
        return max(0, end - start + 1)
