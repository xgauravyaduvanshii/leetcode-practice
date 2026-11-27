# LeetCode 1812. Determine Color of a Chessboard Square — Easy
# https://leetcode.com/problems/determine-color-of-a-chessboard-square/
# Submission 2197599582 — Accepted, Python3
#
# My thinking: on a chessboard, a square is white
# when the column number plus the row number is
# odd. (My first run had the parity flipped and
# came back Wrong Answer; correcting it to odd
# made it Accepted.)

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        col = ord(coordinates[0]) - ord('a') + 1
        row = int(coordinates[1])
        return (col + row) % 2 == 1
