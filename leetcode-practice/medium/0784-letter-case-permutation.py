# LeetCode 784. Letter Case Permutation — Medium
# https://leetcode.com/problems/letter-case-permutation/
# Submission 2198936511 — Accepted, Python3
#
# My thinking: I build the answer one character
# at a time. Digits stay as they are, and every
# letter doubles the list — once lowercase, once
# uppercase.

from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = [""]
        for ch in s:
            if ch.isalpha():
                result = [prefix + letter for prefix in result for letter in (ch.lower(), ch.upper())]
            else:
                result = [prefix + ch for prefix in result]
        return result
