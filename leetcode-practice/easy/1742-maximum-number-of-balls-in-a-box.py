# LeetCode 1742. Maximum Number of Balls in a Box — Easy
# https://leetcode.com/problems/maximum-number-of-balls-in-a-box/
# Submission 2197596621 — Accepted, Python3
#
# My thinking: a ball goes into the box labelled by
# the sum of its digits. I go through every ball
# from low to high, add up its digits, count how
# many balls land in each box, and keep the biggest
# count.

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        counts = {}
        best = 0
        for ball in range(lowLimit, highLimit + 1):
            s = 0
            n = ball
            while n:
                s += n % 10
                n //= 10
            counts[s] = counts.get(s, 0) + 1
            best = max(best, counts[s])
        return best
