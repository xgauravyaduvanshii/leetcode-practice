# LeetCode 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence — Easy
# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
# Submission 2197580066 — Accepted, Python3
#
# My thinking: I split the sentence into words and
# check each one in order — the first word that
# starts with the search word wins, and its
# 1-based position is the answer. If none match,
# I return -1.

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, word in enumerate(sentence.split(), 1):
            if word.startswith(searchWord):
                return i
        return -1
