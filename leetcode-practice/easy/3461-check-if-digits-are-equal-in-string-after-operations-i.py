# 3461. Check if Digits Are Equal in String After Operations I (Easy)
# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/
# Submission 2200019548 — Accepted, Python3
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        # My thinking: each round replaces every
        # neighbouring pair by the last digit of their
        # sum, shrinking the string by one. I keep
        # going until two digits are left, then check
        # whether they match.
        digits = [int(ch) for ch in s]
        while len(digits) > 2:
            digits = [(digits[i] + digits[i + 1]) % 10 for i in range(len(digits) - 1)]
        return digits[0] == digits[1]
