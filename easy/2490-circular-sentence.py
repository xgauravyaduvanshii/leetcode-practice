# LeetCode 2490. Circular Sentence — Easy
# https://leetcode.com/problems/circular-sentence/
# Submission 2197793131 — Accepted, Python3
#
# My thinking: a sentence is circular when the last
# letter of each word matches the first letter of
# the next word — and the last word wraps around to
# the first. I check the ends first, then every
# space boundary.

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False
        for i, ch in enumerate(sentence):
            if ch == ' ' and sentence[i - 1] != sentence[i + 1]:
                return False
        return True
