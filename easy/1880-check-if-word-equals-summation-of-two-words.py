# LeetCode 1880. Check if Word Equals Summation of Two Words — Easy
# https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/
# Submission 2197602799 — Accepted, Python3
#
# My thinking: each letter stands for its position
# in the alphabet (a = 0, b = 1, ...), and a word
# is just those digits read as a number. I convert
# all three words to numbers and check that the
# first two add up to the third.

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def val(w):
            n = 0
            for ch in w:
                n = n * 10 + (ord(ch) - ord('a'))
            return n
        return val(firstWord) + val(secondWord) == val(targetWord)
