# LeetCode 17. Letter Combinations of a Phone Number — Medium
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Submission 2201004549 — Accepted, Python3
#
# My thinking: each digit maps to a few letters, so I
# build every combination by adding one letter at a
# time for each digit in turn.

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        mapping = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
        }
        result = [""]
        for digit in digits:
            result = [prefix + ch for prefix in result for ch in mapping[digit]]
        return result
