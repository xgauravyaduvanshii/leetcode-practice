# 168. Excel Sheet Column Title (Easy)
# https://leetcode.com/problems/excel-sheet-column-title/
# Submission 2199956722 — Accepted, Python3
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # My thinking: column titles are base 26, but
        # there is no zero digit — A means 1, not 0. So
        # before taking each remainder I shift the number
        # down by one, then the letters fall out from the
        # right, one at a time.
        title = []
        n = columnNumber
        while n > 0:
            n -= 1
            title.append(chr(ord("A") + n % 26))
            n //= 26
        return "".join(reversed(title))
