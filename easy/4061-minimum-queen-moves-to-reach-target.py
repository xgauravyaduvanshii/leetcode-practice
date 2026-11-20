# 4061. Minimum Queen Moves to Reach Target (Easy)
# https://leetcode.com/problems/minimum-queen-moves-to-reach-target/
# Submission 2200101554 — Accepted, Python3
class Solution:
    def minQueenMoves(self, source: list[int], target: list[int]) -> int:
        # My thinking: no move is needed when the
        # queen is already there. One move does it
        # when the target shares a row, a column or a
        # diagonal — and any other square is always
        # reachable in two.
        sr, sc = source
        tr, tc = target
        if sr == tr and sc == tc:
            return 0
        if sr == tr or sc == tc or abs(sr - tr) == abs(sc - tc):
            return 1
        return 2
