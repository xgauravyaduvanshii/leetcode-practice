# LeetCode 1408. String Matching in an Array — Easy
# https://leetcode.com/problems/string-matching-in-an-array/
# Submission 2197576633 — Accepted, Python3
#
# My thinking: a word counts if it shows up as a
# substring inside some other word in the list. I
# check every word against every other one, and
# once a match is found I stop checking that word.

class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        result = []
        for i, word in enumerate(words):
            for j, other in enumerate(words):
                if i != j and word in other:
                    result.append(word)
                    break
        return result
