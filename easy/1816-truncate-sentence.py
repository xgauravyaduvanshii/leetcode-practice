# LeetCode 1816. Truncate Sentence — Easy
# https://leetcode.com/problems/truncate-sentence/
# Submission 2197599771 — Accepted, Python3
#
# My thinking: splitting the sentence gives me its
# words in order. I take the first k and join them
# back with single spaces.

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return " ".join(s.split()[:k])
