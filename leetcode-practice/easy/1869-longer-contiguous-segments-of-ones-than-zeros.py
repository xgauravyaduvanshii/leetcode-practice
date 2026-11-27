# LeetCode 1869. Longer Contiguous Segments of Ones than Zeros — Easy
# https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/
# Submission 2197602217 — Accepted, Python3
#
# My thinking: I walk the string tracking the
# longest unbroken run of 1s and the longest run of
# 0s. The answer is true when the longest run of
# 1s is strictly longer.

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        best1 = best0 = cur1 = cur0 = 0
        for ch in s:
            if ch == '1':
                cur1 += 1
                cur0 = 0
                best1 = max(best1, cur1)
            else:
                cur0 += 1
                cur1 = 0
                best0 = max(best0, cur0)
        return best1 > best0
