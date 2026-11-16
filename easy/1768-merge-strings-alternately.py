# LeetCode 1768. Merge Strings Alternately — Easy
# https://leetcode.com/problems/merge-strings-alternately/
# Submission 2197284417 — Accepted, Python3
#
# My thinking: take one letter from the first word,
# then one from the second, and keep going. When
# one word runs out, just stick the rest of the
# other word on the end.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                merged.append(word1[i])
            if i < len(word2):
                merged.append(word2[i])
        return "".join(merged)
