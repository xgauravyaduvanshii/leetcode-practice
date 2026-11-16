# LeetCode 1337. The K Weakest Rows in a Matrix — Easy
# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
# Submission 2197571580 — Accepted, Python3
#
# My thinking: a row's strength is just how many 1's
# it has. I sort the row indexes by their soldier
# count (ties broken by the row number itself) and
# take the first k.

class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        return sorted(range(len(mat)), key=lambda i: (sum(mat[i]), i))[:k]
