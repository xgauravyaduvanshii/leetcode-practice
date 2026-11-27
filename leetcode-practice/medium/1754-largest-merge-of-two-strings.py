# LeetCode 1754. Largest Merge Of Two Strings — Medium
# https://leetcode.com/problems/largest-merge-of-two-strings/
# Submission 2199928100 — Accepted, Python3
#
# My thinking: at each step I take from
# whichever remaining suffix is bigger —
# comparing the whole suffixes, not just the
# next letter, so a later letter can break the
# tie.

class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        result = []
        while i < len(word1) and j < len(word2):
            if word1[i:] > word2[j:]:
                result.append(word1[i])
                i += 1
            else:
                result.append(word2[j])
                j += 1
        result.append(word1[i:])
        result.append(word2[j:])
        return "".join(result)
