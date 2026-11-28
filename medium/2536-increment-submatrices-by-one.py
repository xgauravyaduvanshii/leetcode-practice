# LeetCode 2536. Increment Submatrices by One — Medium
# https://leetcode.com/problems/increment-submatrices-by-one/
# Submission 2205054412 — Accepted, Python3
#
# My thinking: a 2D difference array turns each rectangle update
# into four corner edits, then one prefix-sum pass rebuilds the
# whole matrix. Each query is O(1) and the rebuild is O(n^2).
class Solution:
    def rangeAddQueries(self, n: int, queries: list[list[int]]) -> list[list[int]]:
        diff = [[0] * (n + 1) for _ in range(n + 1)]
        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r1][c2 + 1] -= 1
            diff[r2 + 1][c1] -= 1
            diff[r2 + 1][c2 + 1] += 1
        ans = [[0] * n for _ in range(n)]
        for i in range(n):
            row = 0
            for j in range(n):
                row += diff[i][j]
                ans[i][j] = row + (ans[i - 1][j] if i else 0)
        return ans
