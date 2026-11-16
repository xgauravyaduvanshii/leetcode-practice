# LeetCode 1417. Reformat the String — Easy
# https://leetcode.com/problems/reformat-the-string/
# Submission 2197577759 — Accepted, Python3
#
# My thinking: letters and digits must alternate, so
# their counts can differ by at most 1. I start
# with whichever group is bigger, then weave the
# two together one by one. If the bigger group has
# one extra, it goes at the end.

class Solution:
    def reformat(self, s: str) -> str:
        letters = [ch for ch in s if ch.isalpha()]
        digits = [ch for ch in s if ch.isdigit()]
        if abs(len(letters) - len(digits)) > 1:
            return ""
        if len(letters) >= len(digits):
            first, second = letters, digits
        else:
            first, second = digits, letters
        result = []
        for i in range(len(second)):
            result.append(first[i])
            result.append(second[i])
        if len(first) > len(second):
            result.append(first[-1])
        return "".join(result)
