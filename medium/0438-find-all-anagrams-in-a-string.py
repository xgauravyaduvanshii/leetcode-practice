# LeetCode 438. Find All Anagrams in a String — Medium
# https://leetcode.com/problems/find-all-anagrams-in-a-string/
# Submission 2198795391 — Accepted, Python3
#
# My thinking: I slide a window the same length as
# the pattern and compare letter counts. Each step
# adds the new letter and drops the one that fell
# out of the window — when the counts match, the
# window is an anagram.

from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = Counter(p)
        window = Counter()
        result = []
        for i, char in enumerate(s):
            window[char] += 1
            if i >= len(p):
                left = s[i - len(p)]
                window[left] -= 1
                if window[left] == 0:
                    del window[left]
            if window == need:
                result.append(i - len(p) + 1)
        return result
