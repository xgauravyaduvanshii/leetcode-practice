# LeetCode 130. Surrounded Regions — Medium
# https://leetcode.com/problems/surrounded-regions/
# Submission 2204026582 — Accepted, Python3
#
# My thinking: an 'O' region is only safe when it touches the border,
# so I start a depth-first search from every border 'O' and mark the
# whole connected region as safe with a temporary marker. Any 'O' that
# is left unmarked is fully surrounded, so I flip it to 'X', and then
# I turn the temporary markers back into 'O'. The board is changed in
# place, so the extra memory is just the recursion stack.

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])

        def dfs(r: int, c: int) -> None:
            if r < 0 or r >= m or c < 0 or c >= n:
                return
            if board[r][c] != 'O':
                return
            board[r][c] = '#'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(m):
            dfs(r, 0)
            dfs(r, n - 1)
        for c in range(n):
            dfs(0, c)
            dfs(m - 1, c)

        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'
