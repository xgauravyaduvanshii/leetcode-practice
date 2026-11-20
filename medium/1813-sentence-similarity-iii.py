# LeetCode 1813. Sentence Similarity III — Medium
# https://leetcode.com/problems/sentence-similarity-iii/
# Submission 2199940429 — Accepted, Python3
#
# My thinking: one sentence can only be the
# other with a middle chunk inserted. I match
# words from the front and from the back; if
# the two matches cover the whole short
# sentence, they are similar.

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split()
        words2 = sentence2.split()
        if len(words1) > len(words2):
            words1, words2 = words2, words1
        start = 0
        while start < len(words1) and words1[start] == words2[start]:
            start += 1
        end = 0
        while end < len(words1) - start and words1[len(words1) - 1 - end] == words2[len(words2) - 1 - end]:
            end += 1
        return start + end == len(words1)
