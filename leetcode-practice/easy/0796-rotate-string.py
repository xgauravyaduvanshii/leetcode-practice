# LeetCode 796. Rotate String — Easy
# https://leetcode.com/problems/rotate-string/
# Submission 2197528326 — Accepted, Python3
#
# My thinking: rotating a string just moves its
# start point around. So if goal is a rotation of
# s, then s must appear inside goal written twice
# (goal + goal). The lengths have to match first,
# otherwise it can never work.

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and s in goal + goal
