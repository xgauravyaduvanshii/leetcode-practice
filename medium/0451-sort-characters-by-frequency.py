# LeetCode 451. Sort Characters By Frequency — Medium
# https://leetcode.com/problems/sort-characters-by-frequency/
# Submission 2198804362 — Accepted, Python3
#
# My thinking: I count every character, sort the
# characters by how often they appear, and write
# each one out that many times.

from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join(
            char * count for char, count in Counter(s).most_common()
        )
