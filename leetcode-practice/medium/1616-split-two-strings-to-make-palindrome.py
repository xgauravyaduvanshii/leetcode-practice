# LeetCode 1616. Split Two Strings to Make Palindrome — Medium
# https://leetcode.com/problems/split-two-strings-to-make-palindrome/
# Submission 2199893033 — Accepted, Python3
#
# My thinking: I match the outer characters
# of one string against the other until they
# differ. Whatever is left in the middle only
# needs to be a palindrome on its own, from
# either string.

class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def can_form(first, second):
            left, right = 0, len(first) - 1
            while left < right and first[left] == second[right]:
                left += 1
                right -= 1
            if left >= right:
                return True
            middle = first[left:right + 1]
            return middle == middle[::-1] or second[left:right + 1] == second[left:right + 1][::-1]

        return can_form(a, b) or can_form(b, a)
