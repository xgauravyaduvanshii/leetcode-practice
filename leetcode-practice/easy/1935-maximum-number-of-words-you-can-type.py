# LeetCode 1935. Maximum Number of Words You Can Type — Easy
# https://leetcode.com/problems/maximum-number-of-words-you-can-type/
# Submission 2197604674 — Accepted, Python3
#
# My thinking: a word can be typed only if none of
# its letters is broken. I put the broken letters
# in a set and count the words that contain none of
# them.

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        return sum(1 for word in text.split() if not any(ch in broken for ch in word))
