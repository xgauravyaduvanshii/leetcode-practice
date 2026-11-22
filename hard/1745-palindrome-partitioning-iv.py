# LeetCode 1745. Palindrome Partitioning IV — Hard
# https://leetcode.com/problems/palindrome-partitioning-iv/
# Submission 2201135165 — Accepted, Python3
#
# My thinking: I mark every palindromic substring
# first, then I just need two cut points where all
# three pieces are marked — the first piece, the
# middle piece, and the last piece.

class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True
        for i in range(n):
            for j in range(i + 1, n - 1):
                if is_pal[0][i] and is_pal[i + 1][j] and is_pal[j + 1][n - 1]:
                    return True
        return False
