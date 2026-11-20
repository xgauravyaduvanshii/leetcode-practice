# 3274. Check if Two Chessboard Squares Have the Same Color (Easy)
# https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/
# Submission 2199994108 — Accepted, Python3
class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        # My thinking: a chessboard square's colour is
        # decided by whether its letter plus its number
        # is even or odd. Two squares share a colour
        # exactly when those parities match.
        def parity(coord: str) -> int:
            return (ord(coord[0]) + int(coord[1])) % 2

        return parity(coordinate1) == parity(coordinate2)
