# LeetCode 557. Reverse Words in a String III — Easy
# https://leetcode.com/problems/reverse-words-in-a-string-iii/
# Submission 2197496605 — Accepted, Python3
#
# My thinking: the word order stays the same — only
# the letters inside each word flip. So I split on
# spaces, reverse each word, and join them back
# with single spaces.

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(word[::-1] for word in s.split(" "))
