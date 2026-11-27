# LeetCode 2511. Maximum Enemy Forts That Can Be Captured — Easy
# https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/
# Submission 2197795959 — Accepted, Python3
#
# My thinking: I can only move from a fort I control
# to an enemy fort when everything between them is
# empty. I walk through the forts, remembering the
# last non-empty one, and count the empty spots
# between opposite forts.

class Solution:
    def captureForts(self, forts: list[int]) -> int:
        best = 0
        last = -1
        for i, v in enumerate(forts):
            if v != 0:
                if last != -1 and forts[last] != v:
                    best = max(best, i - last - 1)
                last = i
        return best
