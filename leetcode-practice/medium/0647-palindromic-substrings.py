# LeetCode 647. Palindromic Substrings — Medium
# https://leetcode.com/problems/palindromic-substrings/
# Submission 2198892654 — Accepted, Python3
#
# My thinking: every palindrome has a centre, so I
# try each centre — between two letters as well as
# on one — and expand outward while the letters
# match, counting each match.

class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0
        for center in range(2 * len(s) - 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < len(s) and s[left] == s[right]:
                total += 1
                left -= 1
                right += 1
        return total
