# LeetCode 1662. Check If Two String Arrays are Equivalent — Easy
# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
# Submission 2197592436 — Accepted, Python3
#
# My thinking: the two arrays are equivalent when
# the strings they spell out are the same. I just
# join each array into one string and compare them.

class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        return "".join(word1) == "".join(word2)
