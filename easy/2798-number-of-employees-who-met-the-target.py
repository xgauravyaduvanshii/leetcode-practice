# LeetCode 2798. Number of Employees Who Met the Target — Easy
# https://leetcode.com/problems/number-of-employees-who-met-the-target/
# Submission 2198413131 — Accepted, Python3
#
# My thinking: I just walk the hours list and count
# how many entries reach the target or more. One
# pass is all it takes.

from typing import List


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return sum(1 for h in hours if h >= target)
