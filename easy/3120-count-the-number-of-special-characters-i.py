# 3120. Count the Number of Special Characters I (Easy)
# https://leetcode.com/problems/count-the-number-of-special-characters-i/
# Submission 2199978371 — Accepted, Python3
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # My thinking: a letter is special when it shows
        # up in both cases. I collect the small letters
        # and the capital letters, then count the ones
        # that appear in both sets.
        lower = {ch for ch in word if ch.islower()}
        upper = {ch for ch in word if ch.isupper()}
        return sum(1 for ch in lower if ch.upper() in upper)
