# 3898. Find the Degree of Each Vertex (Easy)
# https://leetcode.com/problems/find-the-degree-of-each-vertex/
# Submission 2200085172 — Accepted, Python3
class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        # My thinking: a vertex's degree is simply how
        # many ones sit in its row of the adjacency
        # matrix.
        return [sum(row) for row in matrix]
