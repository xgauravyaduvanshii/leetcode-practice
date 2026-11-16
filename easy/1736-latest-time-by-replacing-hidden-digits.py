# LeetCode 1736. Latest Time by Replacing Hidden Digits — Easy
# https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/
# Submission 2197596407 — Accepted, Python3
#
# My thinking: I fill each '?' with the biggest digit
# that still keeps the time valid. The hour's first
# digit depends on the second one — '2' only if the
# second digit is at most 3. The minutes are easy:
# the tens place takes '5' and the ones place '9'.

class Solution:
    def maximumTime(self, time: str) -> str:
        t = list(time)
        if t[0] == '?':
            t[0] = '2' if t[1] == '?' or t[1] <= '3' else '1'
        if t[1] == '?':
            t[1] = '3' if t[0] == '2' else '9'
        if t[3] == '?':
            t[3] = '5'
        if t[4] == '?':
            t[4] = '9'
        return "".join(t)
