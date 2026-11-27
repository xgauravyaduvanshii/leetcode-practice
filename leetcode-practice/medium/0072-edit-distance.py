# LeetCode 72. Edit Distance — Medium
# https://leetcode.com/problems/edit-distance/
# Submission 2201011160 — Accepted, Python3
#
# My thinking: I compare the words one letter at a time
# — matching letters cost nothing, anything else is the
# cheapest of inserting, deleting or replacing — and I
# keep only two rows of the table.

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        prev = list(range(len(word2) + 1))
        for i, c1 in enumerate(word1, 1):
            current = [i]
            for j, c2 in enumerate(word2, 1):
                if c1 == c2:
                    current.append(prev[j - 1])
                else:
                    current.append(1 + min(prev[j], current[j - 1], prev[j - 1]))
            prev = current
        return prev[-1]
