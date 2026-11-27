# 3707. Equal Score Substrings (Easy)
# https://leetcode.com/problems/equal-score-substrings/
# Submission 2200045287 — Accepted, Python3
class Solution:
    def scoreBalance(self, s: str) -> bool:
        # My thinking: a letter's score is its place in
        # the alphabet, a is 1 and z is 26. I walk the
        # string adding scores as I go, and check
        # whether the left part ever matches the right
        # part.
        total = sum(ord(ch) - ord("a") + 1 for ch in s)
        left = 0
        for ch in s[:-1]:
            left += ord(ch) - ord("a") + 1
            if left * 2 == total:
                return True
        return False
