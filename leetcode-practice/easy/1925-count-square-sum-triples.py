# LeetCode 1925. Count Square Sum Triples — Easy
# https://leetcode.com/problems/count-square-sum-triples/
# Submission 2197604481 — Accepted, Python3
#
# My thinking: I put all the squares up to n^2 in a
# set, then try every pair (a, b) and check whether
# a^2 + b^2 is also a square in that set. Each
# pair that works is one triple.

class Solution:
    def countTriples(self, n: int) -> int:
        squares = {i * i for i in range(1, n + 1)}
        count = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if a * a + b * b in squares:
                    count += 1
        return count
