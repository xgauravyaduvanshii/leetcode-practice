# LeetCode 344. Reverse String — Easy
# https://leetcode.com/problems/reverse-string/
# Submission 2197464752 — Accepted, Python3
#
# My thinking: two pointers from both ends, swapping
# as they walk towards each other, in place. When
# they meet or cross, the string is reversed.

class Solution:
    def reverseString(self, s: list[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
