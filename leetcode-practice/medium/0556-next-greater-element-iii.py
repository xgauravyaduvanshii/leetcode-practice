# LeetCode 556. Next Greater Element III — Medium
# https://leetcode.com/problems/next-greater-element-iii/
# Submission 2198863248 — Accepted, Python3
#
# My thinking: the next bigger number swaps the
# rightmost digit that can still grow with the
# smallest larger digit after it, then sorts the
# tail ascending. If no digit can grow, or the
# result overflows 32 bits, there is no answer.

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        i = len(digits) - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
        if i < 0:
            return -1
        j = len(digits) - 1
        while digits[j] <= digits[i]:
            j -= 1
        digits[i], digits[j] = digits[j], digits[i]
        digits[i + 1:] = reversed(digits[i + 1:])
        result = int("".join(digits))
        return result if result <= 2**31 - 1 else -1
