# 3908. Valid Digit Number (Easy)
# https://leetcode.com/problems/valid-digit-number/
# Submission 2200086778 — Accepted, Python3
class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        # My thinking: the number is valid when the
        # digit shows up somewhere inside it — but
        # never as its very first digit.
        s = str(n)
        d = str(x)
        return d in s and not s.startswith(d)
