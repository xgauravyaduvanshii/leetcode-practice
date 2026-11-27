# LeetCode 2682. Find the Losers of the Circular Game — Easy
# https://leetcode.com/problems/find-the-losers-of-the-circular-game/
# Submission 2197817733 — Accepted, Python3
#
# My thinking: I simulate the game — the ball moves
# 1*k, then 2*k, then 3*k steps around the circle,
# and I mark each friend who receives it. The game
# stops when the ball reaches someone who already
# got it; everyone never marked is a loser.

from typing import List


class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        seen = [False] * n
        cur = 0
        step = 1
        seen[cur] = True
        while True:
            nxt = (cur + step * k) % n
            if seen[nxt]:
                break
            seen[nxt] = True
            cur = nxt
            step += 1
        return [i + 1 for i in range(n) if not seen[i]]
