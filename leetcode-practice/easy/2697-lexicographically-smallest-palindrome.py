# LeetCode 2697. Lexicographically Smallest Palindrome — Easy
# https://leetcode.com/problems/lexicographically-smallest-palindrome/
# Submission 2197818929 — Accepted, Python3
#
# My thinking: to make a palindrome, each mirrored
# pair of characters must match. To keep it
# lexicographically smallest, I set both characters
# of each pair to the smaller of the two.

class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        a = list(s)
        n = len(a)
        for i in range(n // 2):
            c = min(a[i], a[n - 1 - i])
            a[i] = c
            a[n - 1 - i] = c
        return ''.join(a)
