# LeetCode 1456. Maximum Number of Vowels in a Substring of Given Length — Medium
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
# Submission 2199854039 — Accepted, Python3
#
# My thinking: I slide a window of length k
# across the string, counting vowels inside it.
# Each step adds the letter entering and drops
# the one leaving, and I keep the best count.

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        window = sum(1 for ch in s[:k] if ch in vowels)
        best = window
        for i in range(k, len(s)):
            if s[i] in vowels:
                window += 1
            if s[i - k] in vowels:
                window -= 1
            best = max(best, window)
        return best
