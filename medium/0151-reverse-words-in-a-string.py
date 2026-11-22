# LeetCode 151. Reverse Words in a String — Medium
# https://leetcode.com/problems/reverse-words-in-a-string/
# Submission 2200964558 — Accepted, Python3
#
# My thinking: I split the string into words, which
# throws away the extra spaces, then join them back
# in reverse order with single spaces.

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
