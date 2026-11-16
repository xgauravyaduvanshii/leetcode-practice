# LeetCode 1394. Find Lucky Integer in an Array — Easy
# https://leetcode.com/problems/find-lucky-integer-in-an-array/
# Submission 2197575767 — Accepted, Python3
#
# My thinking: a lucky integer equals its own
# frequency. I count each value, keep the largest
# one that matches its count, and return -1 if
# there is none.

from collections import Counter


class Solution:
    def findLucky(self, arr: list[int]) -> int:
        counts = Counter(arr)
        lucky = -1
        for num, count in counts.items():
            if num == count:
                lucky = max(lucky, num)
        return lucky
