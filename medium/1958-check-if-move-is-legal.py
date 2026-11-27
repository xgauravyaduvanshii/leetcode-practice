# LeetCode 1958. Check if Move is Legal — Medium
# https://leetcode.com/problems/check-if-move-is-legal/
# Submission 2204258271 — Accepted, Python3
#
# My thinking: a move is legal when, in at least one of the eight
# directions, the new piece sits next to a run of one or more
# opponent pieces that is then closed off by one of my own pieces.
# So I walk each direction from the move, counting opponent pieces,
# and the move is legal the moment a walk with at least one opponent
# piece lands on my own colour. An empty cell or the board edge ends
# that direction with no legal line.
class Solution:
    def checkMove(self, board, rMove, cMove, color):
        opponent = "W" if color == "B" else "B"
        for dr, dc in ((-1, -1), (-1, 0), (-1, 1), (0, -1),
                       (0, 1), (1, -1), (1, 0), (1, 1)):
            r, c = rMove + dr, cMove + dc
            seen_opponent = 0
            while 0 <= r < 8 and 0 <= c < 8 and board[r][c] == opponent:
                seen_opponent += 1
                r += dr
                c += dc
            if seen_opponent and 0 <= r < 8 and 0 <= c < 8 and board[r][c] == color:
                return True
        return False
