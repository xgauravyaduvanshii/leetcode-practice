# LeetCode 738. Monotone Increasing Digits — Medium
# https://leetcode.com/problems/monotone-increasing-digits/
# Submission 2198924276 — Accepted, Python3
#
# My thinking: I scan the digits from the right
# and lower the first digit that breaks the climb,
# turning everything after it into nines. That
# gives the largest number that never dips.

class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = list(str(n))
        marker = len(digits)
        for i in range(len(digits) - 1, 0, -1):
            if digits[i] < digits[i - 1]:
                digits[i - 1] = str(int(digits[i - 1]) - 1)
                marker = i
        return int("".join(digits[:marker]) + "9" * (len(digits) - marker))
