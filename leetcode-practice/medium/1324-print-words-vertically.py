# LeetCode 1324. Print Words Vertically — Medium
# https://leetcode.com/problems/print-words-vertically/
# Submission 2199031764 — Accepted, Python3
#
# My thinking: I read the words column by
# column, taking the same letter position from
# each word. Short words leave a space, and the
# trailing spaces of each line are trimmed.

from typing import List


class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        longest = max(len(word) for word in words)
        result = []
        for i in range(longest):
            column = "".join(word[i] if i < len(word) else " " for word in words)
            result.append(column.rstrip())
        return result
