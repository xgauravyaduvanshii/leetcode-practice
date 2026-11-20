# LeetCode 1750. Minimum Length of String After Deleting Similar Ends — Medium
# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/
# Submission 2199927483 — Accepted, Python3
#
# My thinking: while the ends match I strip
# the whole run of that letter from both
# sides. What is left in the middle is the
# answer.

class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        while left < right and s[left] == s[right]:
            ch = s[left]
            while left <= right and s[left] == ch:
                left += 1
            while left <= right and s[right] == ch:
                right -= 1
        return right - left + 1
