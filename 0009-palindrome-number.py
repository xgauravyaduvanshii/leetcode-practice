"""LeetCode 9. Palindrome Number — Easy
https://leetcode.com/problems/palindrome-number/
Submission 2197267708 — Accepted, 11515/11515 testcases, Python3
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        original = x
        reversed_num = 0
        while x > 0:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        return original == reversed_num
