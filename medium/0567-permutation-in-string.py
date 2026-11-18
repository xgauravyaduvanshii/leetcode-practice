# LeetCode 567. Permutation in String — Medium
# https://leetcode.com/problems/permutation-in-string/
# Submission 2198873238 — Accepted, Python3
#
# My thinking: a permutation of the first string
# is just a window of the second with the same
# letter counts. I slide a window of that length
# along and compare the counts as I go.

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        wanted = Counter(s1)
        window = Counter(s2[:len(s1)])
        if window == wanted:
            return True
        for i in range(len(s1), len(s2)):
            window[s2[i]] += 1
            window[s2[i - len(s1)]] -= 1
            if window[s2[i - len(s1)]] == 0:
                del window[s2[i - len(s1)]]
            if window == wanted:
                return True
        return False
