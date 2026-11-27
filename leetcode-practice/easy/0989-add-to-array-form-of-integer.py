# LeetCode 989. Add to Array-Form of Integer — Easy
# https://leetcode.com/problems/add-to-array-form-of-integer/
# Submission 2197548303 — Accepted, Python3
#
# My thinking: I add k to the number digit by digit
# from the right, the same way I would on paper —
# add the digit to k, keep the last digit of the
# result, and carry the rest over to the next
# digit. Whatever is left of k at the end becomes
# the leading digits.

class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        result = []
        i = len(num) - 1
        while i >= 0 or k > 0:
            if i >= 0:
                k += num[i]
                i -= 1
            result.append(k % 10)
            k //= 10
        return result[::-1]
