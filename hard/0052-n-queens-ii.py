# LeetCode 52. N-Queens II — Hard
# https://leetcode.com/problems/n-queens-ii/
# Submission 2198379467 — Accepted, Python3
#
# My thinking: same walk as N-Queens, but I only
# count the finished boards instead of saving
# them. I place queens row by row, skipping any
# column or diagonal that is already attacked, and
# every time I fill the last row the count goes up
# by one.

class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0
        cols = set()
        diag_down = set()
        diag_up = set()

        def backtrack(row: int) -> None:
            nonlocal count
            if row == n:
                count += 1
                return
            for col in range(n):
                if col in cols or (row - col) in diag_down or (row + col) in diag_up:
                    continue
                cols.add(col)
                diag_down.add(row - col)
                diag_up.add(row + col)
                backtrack(row + 1)
                cols.remove(col)
                diag_down.remove(row - col)
                diag_up.remove(row + col)

        backtrack(0)
        return count
