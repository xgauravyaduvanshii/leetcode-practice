# LeetCode 2108. Find First Palindromic String in the Array — Easy
# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/
# Submission 2197613496 — Accepted, Python3
#
# My thinking: I go through the words in order and
# return the first one that reads the same forwards
# and backwards. If none is a palindrome, the answer
# is an empty string.

class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for w in words:
            if w == w[::-1]:
                return w
        return ""
