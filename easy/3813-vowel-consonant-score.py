# 3813. Vowel-Consonant Score (Easy)
# https://leetcode.com/problems/vowel-consonant-score/
# Submission 2200068344 — Accepted, Python3
class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        # My thinking: count the vowels and the
        # consonants — spaces and digits are neither.
        # The score is how many whole times the
        # consonants fit into the vowels, or zero when
        # there are no consonants at all.
        vowels = set("aeiou")
        v = sum(1 for ch in s if ch in vowels)
        c = sum(1 for ch in s if ch.isalpha() and ch not in vowels)
        return v // c if c > 0 else 0
