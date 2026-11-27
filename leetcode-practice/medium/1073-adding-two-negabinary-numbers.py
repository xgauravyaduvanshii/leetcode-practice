# LeetCode 1073. Adding Two Negabinary Numbers — Medium
# https://leetcode.com/problems/adding-two-negabinary-numbers/
# Submission 2198996700 — Accepted, Python3
#
# My thinking: I add the numbers bit by bit from
# the right, just like normal addition — except
# a carry of two in base minus two becomes a
# carry of minus one to the next place.

from typing import List


class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        carry = 0
        i, j = len(arr1) - 1, len(arr2) - 1
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += arr1[i]
                i -= 1
            if j >= 0:
                total += arr2[j]
                j -= 1
            result.append(total & 1)
            carry = -(total >> 1)
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        return result[::-1]
