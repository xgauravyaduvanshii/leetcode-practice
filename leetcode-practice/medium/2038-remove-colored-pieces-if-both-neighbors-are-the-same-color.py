# LeetCode 2038. Remove Colored Pieces if Both Neighbors are the Same Color — Medium
# https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/
# Submission 2204374264 — Accepted, Python3
#
# My thinking: a piece can only be removed while it sits inside a run
# of at least three equal colours, and removing pieces from the middle
# of a run never creates a new removable piece for the other player.
# So each run of length L gives its owner exactly L - 2 moves, Alice
# counts the moves from 'A' runs, Bob from 'B' runs, and Alice wins
# when she has strictly more moves, since she moves first.
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a = b = 0
        n = len(colors)
        i = 0
        while i < n:
            j = i
            while j < n and colors[j] == colors[i]:
                j += 1
            moves = max(0, j - i - 2)
            if colors[i] == 'A':
                a += moves
            else:
                b += moves
            i = j
        return a > b
