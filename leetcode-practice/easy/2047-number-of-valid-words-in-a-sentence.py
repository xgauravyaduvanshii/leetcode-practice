# LeetCode 2047. Number of Valid Words in a Sentence — Easy
# https://leetcode.com/problems/number-of-valid-words-in-a-sentence/
# Submission 2197610499 — Accepted, Python3
#
# My thinking: a valid word is lowercase letters,
# with at most one hyphen between letters and at
# most one punctuation mark (!, . or ,) at the end
# — and a lone punctuation mark also counts. I
# check each token against that pattern.

import re


class Solution:
    def countValidWords(self, sentence: str) -> int:
        pattern = re.compile(r'^([a-z]+(-[a-z]+)?)?[!.,]?$')
        return sum(1 for w in sentence.split() if pattern.match(w))
