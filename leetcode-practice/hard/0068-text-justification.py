# LeetCode 68. Text Justification — Hard
# https://leetcode.com/problems/text-justification/
# Submission 2198381327 — Accepted, Python3
#
# My thinking: I pack words into a line until the
# next word would not fit. For a full line I spread
# the leftover spaces across the gaps, giving the
# left gaps one extra space when they do not divide
# evenly. The last line and a line with a single
# word are left-justified instead, with the empty
# space padded on the right.

from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        i = 0
        while i < len(words):
            j = i
            line_len = 0
            while j < len(words) and line_len + len(words[j]) + (j - i) <= maxWidth:
                line_len += len(words[j])
                j += 1
            line_words = words[i:j]
            gaps = len(line_words) - 1
            if j == len(words) or gaps == 0:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            else:
                spaces = maxWidth - line_len
                base, extra = divmod(spaces, gaps)
                line = ""
                for k, word in enumerate(line_words):
                    line += word
                    if k < gaps:
                        line += " " * (base + (1 if k < extra else 0))
            lines.append(line)
            i = j
        return lines
