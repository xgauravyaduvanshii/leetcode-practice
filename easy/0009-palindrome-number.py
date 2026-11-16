# LeetCode 9. Palindrome Number — Easy
# https://leetcode.com/problems/palindrome-number/
# Submission 2197267708 — Accepted, Python3
#
# My thinking: a negative number can never be a palindrome
# because of the minus sign. For the rest, I build the
# number backwards, digit by digit, and check if it
# matches the original.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        original = x
        reversed_number = 0

        while x > 0:
            last_digit = x % 10
            reversed_number = reversed_number * 10 + last_digit
            x = x // 10

        return original == reversed_number
