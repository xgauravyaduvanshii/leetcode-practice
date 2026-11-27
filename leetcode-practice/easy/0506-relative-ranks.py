# LeetCode 506. Relative Ranks — Easy
# https://leetcode.com/problems/relative-ranks/
# Submission 2197486794 — Accepted, Python3
#
# My thinking: I sort the athletes by score, biggest
# first, and remember each one's original position.
# Then the first three get Gold, Silver and Bronze,
# and everyone else just gets their rank number.

class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        order = sorted(range(len(score)), key=lambda i: score[i], reverse=True)
        result = [""] * len(score)
        for rank, idx in enumerate(order):
            if rank == 0:
                result[idx] = "Gold Medal"
            elif rank == 1:
                result[idx] = "Silver Medal"
            elif rank == 2:
                result[idx] = "Bronze Medal"
            else:
                result[idx] = str(rank + 1)
        return result
