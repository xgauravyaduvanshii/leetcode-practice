# LeetCode 409. Longest Palindrome — Easy
# https://leetcode.com/problems/longest-palindrome/
# Submission 2197472957 — Accepted, Python3
#
# My thinking: I count each letter. Pairs of the
# same letter can go on both sides of the palindrome,
# so I take the even part of every count. If any
# letter has an odd count, I can put one of those
# in the middle as well — just one.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1
        length = 0
        odd_found = False
        for count in counts.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                odd_found = True
        if odd_found:
            length += 1
        return length
