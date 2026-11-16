# LeetCode 383. Ransom Note — Easy
# https://leetcode.com/problems/ransom-note/
# Submission 2197287167 — Accepted, Python3
#
# My thinking: I count the letters I have in the
# magazine first. Then I go through the ransom note
# letter by letter — every letter I need has to be
# there, and I use it up once. If I run out, the
# note cannot be built.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        available = Counter(magazine)

        for letter in ransomNote:
            if available[letter] <= 0:
                return False
            available[letter] -= 1

        return True
