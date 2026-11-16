# LeetCode 884. Uncommon Words from Two Sentences — Easy
# https://leetcode.com/problems/uncommon-words-from-two-sentences/
# Submission 2197538045 — Accepted, Python3
#
# My thinking: I join both sentences together and
# count how many times each word appears. A word
# is uncommon if it shows up exactly once across
# both sentences — so I return all words with a
# count of one.

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        counts = {}
        for word in (s1 + " " + s2).split():
            counts[word] = counts.get(word, 0) + 1
        return [word for word, count in counts.items() if count == 1]
