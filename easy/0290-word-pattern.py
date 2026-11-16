# LeetCode 290. Word Pattern — Easy
# https://leetcode.com/problems/word-pattern/
# Submission 2197462044 — Accepted, Python3
#
# My thinking: same idea as isomorphic strings — the
# mapping has to work both ways. Each pattern letter
# must always map to the same word, and each word
# must always come from the same letter. If the
# counts do not even match, it fails straight away.

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        char_to_word = {}
        word_to_char = {}
        for char, word in zip(pattern, words):
            if char in char_to_word and char_to_word[char] != word:
                return False
            if word in word_to_char and word_to_char[word] != char:
                return False
            char_to_word[char] = word
            word_to_char[word] = char
        return True
