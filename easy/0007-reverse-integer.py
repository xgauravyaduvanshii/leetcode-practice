# LeetCode 7. Reverse Integer — Easy
# https://leetcode.com/problems/reverse-integer/
# Submission 2197382231 — Accepted, Python3
#
# My thinking: I strip the sign off, reverse the digits
# as a string, then put the sign back on. If the result
# falls outside the 32-bit signed range, the answer is 0.

class Solution:
    def reverse(self, x: int) -> int:
        # Flip the sign off, reverse the digits as a string, then put the sign back.
        sign = -1 if x < 0 else 1
        rev = int(str(abs(x))[::-1]) * sign
        # 32-bit signed range check — out of range means 0.
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev
