# LeetCode 2085. Count Common Words With One Occurrence — Easy
# https://leetcode.com/problems/count-common-words-with-one-occurrence/
# Submission 2197612152 — Accepted, Python3
#
# My thinking: I count each word in both lists, then
# count the words that appear exactly once in the
# first list and exactly once in the second.

from collections import Counter


class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        c1 = Counter(words1)
        c2 = Counter(words2)
        return sum(1 for w in c1 if c1[w] == 1 and c2[w] == 1)
