# LeetCode 1704. Determine if String Halves Are Alike — Easy
# https://leetcode.com/problems/determine-if-string-halves-are-alike/
# Submission 2197594668 — Accepted, Python3
#
# My thinking: I split the string in half and count
# the vowels in each half. If the two counts match,
# the halves are alike.

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set("aeiouAEIOU")
        half = len(s) // 2
        a = sum(1 for ch in s[:half] if ch in vowels)
        b = sum(1 for ch in s[half:] if ch in vowels)
        return a == b
