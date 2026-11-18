# LeetCode 816. Ambiguous Coordinates — Medium
# https://leetcode.com/problems/ambiguous-coordinates/
# Submission 2198946824 — Accepted, Python3
#
# My thinking: I try every place to split the
# digits into two numbers, and for each half I
# list every way to put a decimal point in it —
# no leading zeros, no trailing zeros after the
# point.

from typing import List


class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def splits(text):
            options = []
            if len(text) == 1 or text[0] != "0":
                options.append(text)
            for i in range(1, len(text)):
                whole, frac = text[:i], text[i:]
                if (len(whole) == 1 or whole[0] != "0") and frac[-1] != "0":
                    options.append(whole + "." + frac)
            return options

        inner = s[1:-1]
        result = []
        for i in range(1, len(inner)):
            for left in splits(inner[:i]):
                for right in splits(inner[i:]):
                    result.append(f"({left}, {right})")
        return result
