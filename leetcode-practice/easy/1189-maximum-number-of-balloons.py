# LeetCode 1189. Maximum Number of Balloons — Easy
# https://leetcode.com/problems/maximum-number-of-balloons/
# Submission 2197562418 — Accepted, Python3
#
# My thinking: the word "balloon" needs one b, one a,
# two l's, two o's and one n. I count the letters
# in the text and see how many full sets I can make
# — the scarcest letter (halving l and o, since
# they are needed twice) decides the answer.

from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = Counter(text)
        return min(
            counts["b"],
            counts["a"],
            counts["l"] // 2,
            counts["o"] // 2,
            counts["n"],
        )
