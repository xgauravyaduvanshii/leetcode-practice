# LeetCode 917. Reverse Only Letters — Easy
# https://leetcode.com/problems/reverse-only-letters/
# Submission 2197542139 — Accepted, Python3
#
# My thinking: two pointers from the ends. I skip
# anything that is not a letter, and when both
# pointers sit on letters I swap them. The
# non-letters never move, so they stay exactly
# where they were.

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        chars = list(s)
        left, right = 0, len(chars) - 1
        while left < right:
            if not chars[left].isalpha():
                left += 1
            elif not chars[right].isalpha():
                right -= 1
            else:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
        return "".join(chars)
