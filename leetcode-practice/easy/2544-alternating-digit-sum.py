# LeetCode 2544. Alternating Digit Sum — Easy
# https://leetcode.com/problems/alternating-digit-sum/
# Submission 2197800820 — Accepted, Python3
#
# My thinking: I add the first digit, subtract the
# second, add the third, and so on — the sign
# alternates with the position of each digit.

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = str(n)
        total = 0
        for i, ch in enumerate(s):
            total += int(ch) if i % 2 == 0 else -int(ch)
        return total
