# LeetCode 1523. Count Odd Numbers in an Interval Range — Easy
# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
# Submission 2197584181 — Accepted, Python3
#
# My thinking: the count of odd numbers up to a
# number is simple — (x + 1) // 2. So the odds
# between low and high are just the odds up to
# high minus the odds below low.

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2
