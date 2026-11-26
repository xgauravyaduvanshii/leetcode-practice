# LeetCode 12. Integer to Roman — Medium
# https://leetcode.com/problems/integer-to-roman/
# Submission 2203803226 — Accepted, Python3
#
# My thinking: I walk the Roman symbols from largest to smallest and
# take as many of each as fit, which works because the symbols are
# listed in decreasing value and the subtractive pairs (IV, IX, XL,
# XC, CD, CM) are included as symbols of their own. Whatever is left
# after one symbol is handled by the smaller ones.

class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'),
        ]
        out = []
        for value, symbol in symbols:
            count, num = divmod(num, value)
            out.append(symbol * count)
        return ''.join(out)
