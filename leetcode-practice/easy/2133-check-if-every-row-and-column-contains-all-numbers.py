# LeetCode 2133. Check if Every Row and Column Contains All Numbers — Easy
# https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/
# Submission 2197614427 — Accepted, Python3
#
# My thinking: a valid matrix has every row and every
# column containing exactly the numbers 1 through n.
# I check each row and each column as a set against
# that target set.

class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:
        n = len(matrix)
        target = set(range(1, n + 1))
        for i in range(n):
            if set(matrix[i]) != target:
                return False
            if set(matrix[r][i] for r in range(n)) != target:
                return False
        return True
