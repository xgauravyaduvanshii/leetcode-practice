# LeetCode 2326. Spiral Matrix IV — Medium
# https://leetcode.com/problems/spiral-matrix-iv/
# Submission 2204690185 — Accepted, Python3
#
# My thinking: fill a matrix with -1 and walk it in a spiral — right,
# down, left, up — writing each linked-list value into the current cell.
# Before stepping to the next cell I check it is inside the matrix and
# still -1; if not, I turn clockwise and step in the new direction. When
# the list runs out, the unwritten cells stay -1.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: ListNode | None) -> list[list[int]]:
        mat = [[-1] * n for _ in range(m)]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        i = j = 0
        node = head
        while node:
            mat[i][j] = node.val
            node = node.next
            ni, nj = i + dirs[d][0], j + dirs[d][1]
            if not (0 <= ni < m and 0 <= nj < n and mat[ni][nj] == -1):
                d = (d + 1) % 4
                ni, nj = i + dirs[d][0], j + dirs[d][1]
            i, j = ni, nj
        return mat
