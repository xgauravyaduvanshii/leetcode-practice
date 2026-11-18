# LeetCode 212. Word Search II — Hard
# https://leetcode.com/problems/word-search-ii/
# Submission 2198393739 — Accepted, Python3
#
# My thinking: I pack all the words into a trie so
# every path on the board only follows real word
# prefixes. From each cell I walk the trie letter by
# letter, marking cells used as I go so no cell is
# visited twice in one word. When I reach a word's
# end I save it and remove that ending, so the same
# word is never reported twice.

from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = {}
        for word in words:
            node = root
            for ch in word:
                node = node.setdefault(ch, {})
            node["#"] = word
        m, n = len(board), len(board[0])
        found = []

        def dfs(i: int, j: int, node) -> None:
            ch = board[i][j]
            if ch not in node:
                return
            node = node[ch]
            if "#" in node:
                found.append(node.pop("#"))
            board[i][j] = "."
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != ".":
                    dfs(ni, nj, node)
            board[i][j] = ch

        for i in range(m):
            for j in range(n):
                dfs(i, j, root)
        return found
