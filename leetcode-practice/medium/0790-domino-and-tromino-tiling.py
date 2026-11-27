# LeetCode 790. Domino and Tromino Tiling — Medium
# https://leetcode.com/problems/domino-and-tromino-tiling/
# Submission 2198938437 — Accepted, Python3
#
# My thinking: I track two states — a fully
# filled board and one with a single missing
# cell. A full board grows by one vertical
# domino, two horizontals, or a tromino filling
# the gap; the gap state grows from a full board
# or from another gap.

class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        mod = 10 ** 9 + 7
        full = [0] * (n + 1)
        gap = [0] * (n + 1)
        full[0], full[1], full[2] = 1, 1, 2
        gap[1], gap[2] = 0, 1
        for i in range(3, n + 1):
            full[i] = (full[i - 1] + full[i - 2] + 2 * gap[i - 1]) % mod
            gap[i] = (full[i - 2] + gap[i - 1]) % mod
        return full[n]
