# LeetCode 1025. Divisor Game — Easy
# https://leetcode.com/problems/divisor-game/
# Submission 2197552284 — Accepted, Python3
#
# My thinking: the trick is parity. If n is even,
# Alice can always subtract 1 (which is a divisor)
# and hand Bob an odd number; Bob's every move
# then hands back an even number, so Alice gets
# the last move. If n is odd, the same logic works
# against her — so she wins exactly when n is even.

class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0
