# LeetCode 1328. Break a Palindrome — Medium
# https://leetcode.com/problems/break-a-palindrome/
# Submission 2199032325 — Accepted, Python3
#
# My thinking: changing the first non-a letter
# in the first half to a breaks the palindrome
# with the smallest result. If the first half
# is all a, the last letter becomes b instead.

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""
        chars = list(palindrome)
        for i in range(n // 2):
            if chars[i] != "a":
                chars[i] = "a"
                return "".join(chars)
        chars[-1] = "b"
        return "".join(chars)
