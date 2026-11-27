# LeetCode 1654. Minimum Jumps to Reach Home — Medium
# https://leetcode.com/problems/minimum-jumps-to-reach-home/
# Submission 2199901836 — Accepted, Python3
#
# My thinking: I search level by level from
# home, remembering each position plus whether
# I just jumped back — two backs in a row are
# not allowed. The first time I land on x,
# the jump count is the answer.

from collections import deque
from typing import List


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        limit = max(x, max(forbidden, default=0)) + a + b
        queue = deque([(0, False)])
        seen = {(0, False)}
        jumps = 0
        while queue:
            for _ in range(len(queue)):
                pos, went_back = queue.popleft()
                if pos == x:
                    return jumps
                forward = pos + a
                if forward <= limit and forward not in forbidden and (forward, False) not in seen:
                    seen.add((forward, False))
                    queue.append((forward, False))
                if not went_back:
                    back = pos - b
                    if back >= 0 and back not in forbidden and (back, True) not in seen:
                        seen.add((back, True))
                        queue.append((back, True))
            jumps += 1
        return -1
