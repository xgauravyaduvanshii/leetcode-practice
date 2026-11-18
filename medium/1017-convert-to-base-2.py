# LeetCode 1017. Convert to Base -2 — Medium
# https://leetcode.com/problems/convert-to-base-2/
# Submission 2198987108 — Accepted, Python3
#
# My thinking: I take the lowest bit, then divide
# by minus two — which is the same as shifting
# right and negating. Each bit lands in the
# string, reversed at the end.

class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        digits = []
        while n != 0:
            digits.append(str(n & 1))
            n = -(n >> 1)
        return "".join(reversed(digits))
