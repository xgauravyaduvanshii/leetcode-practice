# LeetCode 1332. Remove Palindromic Subsequences — Easy
# https://leetcode.com/problems/remove-palindromic-subsequences/
# Submission 2197571311 — Accepted, Python3
#
# My thinking: the string only has a's and b's, so I
# can always remove all the a's in one go (they
# form a palindrome) and then all the b's. If the
# whole string is already a palindrome, one step
# does it; otherwise two steps always work.

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s:
            return 0
        return 1 if s == s[::-1] else 2
