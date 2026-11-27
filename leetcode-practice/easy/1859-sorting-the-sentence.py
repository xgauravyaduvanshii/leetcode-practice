# LeetCode 1859. Sorting the Sentence — Easy
# https://leetcode.com/problems/sorting-the-sentence/
# Submission 2197601736 — Accepted, Python3
#
# My thinking: every word ends with its position
# number. I sort the words by that trailing digit
# and join them back, dropping the numbers.

class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        words.sort(key=lambda w: int(w[-1]))
        return " ".join(w[:-1] for w in words)
