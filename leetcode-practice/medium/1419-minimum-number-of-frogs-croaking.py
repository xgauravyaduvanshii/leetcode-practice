# LeetCode 1419. Minimum Number of Frogs Croaking — Medium
# https://leetcode.com/problems/minimum-number-of-frogs-croaking/
# Submission 2199055903 — Accepted, Python3
#
# My thinking: I count how many frogs have
# started each letter of "croak". A letter can
# only sound when a frog is waiting on the
# letter before it, and a finished frog is free
# to start again — the most frogs ever waiting
# at once is the answer.

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        c = r = o = a = k = 0
        frogs = 0
        for ch in croakOfFrogs:
            if ch == "c":
                c += 1
                frogs = max(frogs, c)
            elif ch == "r":
                r += 1
                if r > c:
                    return -1
            elif ch == "o":
                o += 1
                if o > r:
                    return -1
            elif ch == "a":
                a += 1
                if a > o:
                    return -1
            else:
                k += 1
                if k > a:
                    return -1
                c -= 1
                r -= 1
                o -= 1
                a -= 1
                k -= 1
        return frogs if c == 0 else -1
