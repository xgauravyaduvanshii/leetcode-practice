# LeetCode 1002. Find Common Characters — Easy
# https://leetcode.com/problems/find-common-characters/
# Submission 2197550055 — Accepted, Python3
#
# My thinking: I count the letters of the first word.
# For each next word, I count its letters too and
# keep only the smaller count for each letter — a
# letter can only appear in all words as many
# times as its smallest count. At the end I expand
# the counts back into a list.

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        common = {}
        for ch in words[0]:
            common[ch] = common.get(ch, 0) + 1
        for word in words[1:]:
            counts = {}
            for ch in word:
                counts[ch] = counts.get(ch, 0) + 1
            for ch in list(common):
                common[ch] = min(common[ch], counts.get(ch, 0))
        result = []
        for ch, count in common.items():
            result.extend([ch] * count)
        return result
