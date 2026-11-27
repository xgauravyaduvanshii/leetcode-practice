# LeetCode 5. Longest Palindromic Substring — Medium
# https://leetcode.com/problems/longest-palindromic-substring/
# Submission 2203752938 — Accepted, Python3

# My thinking:
# A palindrome reads the same forwards and backwards, so every palindrome
# has a center. I try every position as a center and expand outwards as
# long as the characters on both sides match, keeping the longest one found.
# Each center needs two expansions: odd length (center is one character)
# and even length (center is between two characters). If the whole string
# is already a palindrome I return it straight away — that also avoids the
# slow case of a long all-same-character input, where expanding would be
# quadratic anyway but with a trivial answer.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        n = len(s)
        start = 0
        max_len = 1
        for center in range(n):
            # Odd-length palindromes: center is one character.
            l = r = center
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > max_len:
                    start = l
                    max_len = r - l + 1
                l -= 1
                r += 1
            # Even-length palindromes: center is between two characters.
            l, r = center, center + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > max_len:
                    start = l
                    max_len = r - l + 1
                l -= 1
                r += 1
        return s[start:start + max_len]
