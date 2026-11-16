# LeetCode 2114. Maximum Number of Words Found in Sentences — Easy
# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/
# Submission 2197613681 — Accepted, Python3
#
# My thinking: the number of words in a sentence is
# the number of pieces it splits into. I count that
# for every sentence and take the maximum.

class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        return max(len(s.split()) for s in sentences)
