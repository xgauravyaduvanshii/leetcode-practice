# 3856. Trim Trailing Vowels (Easy)
# https://leetcode.com/problems/trim-trailing-vowels/
# Submission 2200076472 — Accepted, Python3
class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        # My thinking: keep cutting vowels off the end
        # until the last letter is a consonant — or
        # nothing is left at all.
        return s.rstrip("aeiou")
