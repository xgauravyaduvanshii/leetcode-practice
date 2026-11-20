# 3136. Valid Word (Easy)
# https://leetcode.com/problems/valid-word/
# Submission 2199979155 — Accepted, Python3
class Solution:
    def isValid(self, word: str) -> bool:
        # My thinking: a valid word is at least three
        # characters, made only of letters and digits,
        # with at least one vowel and at least one
        # consonant. Any other character, or a missing
        # vowel or consonant, makes it invalid.
        if len(word) < 3:
            return False
        vowels = set("aeiouAEIOU")
        has_vowel = False
        has_consonant = False
        for ch in word:
            if not ch.isalnum():
                return False
            if ch.isalpha():
                if ch in vowels:
                    has_vowel = True
                else:
                    has_consonant = True
        return has_vowel and has_consonant
