# LeetCode 1451. Rearrange Words in a Sentence — Medium
# https://leetcode.com/problems/rearrange-words-in-a-sentence/
# Submission 2199853612 — Accepted, Python3
#
# My thinking: I sort the words by length —
# a stable sort keeps equal-length words in
# their old order. The first word starts
# capitalised, so I lower it before sorting
# and capitalise the new first word after.

class Solution:
    def arrangeWords(self, text: str) -> str:
        words = (text[0].lower() + text[1:]).split()
        words.sort(key=len)
        result = " ".join(words)
        return result[0].upper() + result[1:]
