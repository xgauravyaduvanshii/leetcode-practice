# LeetCode 1716. Calculate Money in Leetcode Bank — Easy
# https://leetcode.com/problems/calculate-money-in-leetcode-bank/
# Submission 2197595121 — Accepted, Python3
#
# My thinking: each week starts one dollar higher
# than the last, and within a week the deposit
# grows by one each day. I just simulate week by
# week, day by day, until I have counted n days.

class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        week = 0
        while n > 0:
            for day in range(7):
                if n == 0:
                    break
                total += week + 1 + day
                n -= 1
            week += 1
        return total
