# LeetCode 926. Flip String to Monotone Increasing — Medium
# https://leetcode.com/problems/flip-string-to-monotone-increasing/
# Submission 2198970297 — Accepted, Python3
#
# My thinking: I scan the string keeping the
# ones I have seen. Each zero after a one must
# be flipped — unless I flip one of those ones
# instead, which is the same cost, so I spend
# one flip per such zero and move on.

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones = 0
        flips = 0
        for ch in s:
            if ch == "1":
                ones += 1
            elif ones > 0:
                flips += 1
                ones -= 1
        return flips
