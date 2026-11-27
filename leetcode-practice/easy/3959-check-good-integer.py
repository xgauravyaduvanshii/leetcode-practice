# 3959. Check Good Integer (Easy)
# https://leetcode.com/problems/check-good-integer/
# Submission 2200091691 — Accepted, Python3
class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        # My thinking: add up the digits, and add up
        # their squares too. The number is good when
        # the squares beat the plain sum by fifty or
        # more.
        digits = [int(d) for d in str(n)]
        return sum(d * d for d in digits) - sum(digits) >= 50
