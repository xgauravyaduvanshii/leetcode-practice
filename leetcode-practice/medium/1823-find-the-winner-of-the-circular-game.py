# LeetCode 1823. Find the Winner of the Circular Game — Medium
# https://leetcode.com/problems/find-the-winner-of-the-circular-game/
# Submission 2199941763 — Accepted, Python3
#
# My thinking: the classic Josephus answer
# builds up from a single player — each time
# the circle grows by one, the winner shifts
# forward by k.

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 0
        for size in range(2, n + 1):
            winner = (winner + k) % size
        return winner + 1
