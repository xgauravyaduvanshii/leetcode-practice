# LeetCode 520. Detect Capital — Easy
# https://leetcode.com/problems/detect-capital/
# Submission 2197488297 — Accepted, Python3
#
# My thinking: a word uses capitals correctly in
# exactly three ways — all capitals, all lowercase,
# or only the first letter capital. Python's
# isupper, islower and istitle check exactly those
# three.

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()
