# LeetCode 125. Valid Palindrome — Easy
# https://leetcode.com/problems/valid-palindrome/
# Submission 2197443464 — Accepted, Python3
#
# My thinking: two pointers, one from each end. I skip
# anything that is not a letter or a digit, and compare
# what is left in lowercase. If any pair does not match,
# it is not a palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
