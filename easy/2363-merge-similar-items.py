# LeetCode 2363. Merge Similar Items — Easy
# https://leetcode.com/problems/merge-similar-items/
# Submission 2197774629 — Accepted, Python3
#
# My thinking: I add up the weights of items with the
# same value from both lists, then return the merged
# items sorted by value.

class Solution:
    def mergeSimilarItems(self, items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
        d = {}
        for v, w in items1 + items2:
            d[v] = d.get(v, 0) + w
        return sorted([v, w] for v, w in d.items())
