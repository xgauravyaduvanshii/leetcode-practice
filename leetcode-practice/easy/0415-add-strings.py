# LeetCode 415. Add Strings — Easy
# https://leetcode.com/problems/add-strings/
# Submission 2197475092 — Accepted, Python3
#
# My thinking: I add the two numbers digit by digit
# from the right, the way I would on paper — each
# column gives a digit and a carry to the next one.
# I keep going while either number still has digits
# left, or there is a carry.

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = []
        while i >= 0 or j >= 0 or carry:
            d1 = ord(num1[i]) - ord('0') if i >= 0 else 0
            d2 = ord(num2[j]) - ord('0') if j >= 0 else 0
            total = d1 + d2 + carry
            result.append(str(total % 10))
            carry = total // 10
            i -= 1
            j -= 1
        return "".join(reversed(result))
