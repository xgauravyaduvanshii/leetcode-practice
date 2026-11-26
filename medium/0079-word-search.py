# LeetCode 79. Word Search — Medium
# https://leetcode.com/problems/word-search/
# Submission 2203848111 — Accepted, Python3
#
# My thinking: I try every cell as a starting point and search
# depth-first, marking each cell used while I am on it and unmarking
# it when I backtrack, so no cell is reused in one word. Before
# searching I flip the word when its last letter is rarer on the board
# than its first, which prunes the slow case where the search starts
# from a very common letter.

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        from collections import Counter
        counts = Counter(ch for row in board for ch in row)
        if counts[word[0]] > counts[word[-1]]:
            word = word[::-1]
        m, n = len(board), len(board[0])

        def dfs(r: int, c: int, k: int) -> bool:
            if k == len(word):
                return True
            if r < 0 or r >= m or c < 0 or c >= n:
                return False
            if board[r][c] != word[k]:
                return False
            saved = board[r][c]
            board[r][c] = '#'
            found = (
                dfs(r + 1, c, k + 1)
                or dfs(r - 1, c, k + 1)
                or dfs(r, c + 1, k + 1)
                or dfs(r, c - 1, k + 1)
            )
            board[r][c] = saved
            return found

        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        return False
