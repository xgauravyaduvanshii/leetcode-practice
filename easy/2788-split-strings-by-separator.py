# LeetCode 2788. Split Strings by Separator — Easy
# https://leetcode.com/problems/split-strings-by-separator/
# Submission 2198412122 — Accepted, Python3
#
# My thinking: I split each word on the separator
# and keep only the non-empty pieces, in order.
# Splitting gives empty strings where separators
# sit next to each other or at the ends, and those
# are simply dropped.

from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        answer = []
        for word in words:
            for part in word.split(separator):
                if part:
                    answer.append(part)
        return answer
