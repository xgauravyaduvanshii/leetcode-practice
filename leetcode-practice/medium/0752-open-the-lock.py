# LeetCode 752. Open the Lock — Medium
# https://leetcode.com/problems/open-the-lock/
# Submission 2198929234 — Accepted, Python3
#
# My thinking: each dial turn is one move, so a
# breadth-first search finds the shortest path to
# the target. I skip the dead ends and never
# visit a combination twice.

from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1
        queue = deque([("0000", 0)])
        seen = {"0000"}
        while queue:
            current, steps = queue.popleft()
            if current == target:
                return steps
            for i in range(4):
                digit = int(current[i])
                for change in (-1, 1):
                    next_digit = (digit + change) % 10
                    nxt = current[:i] + str(next_digit) + current[i + 1:]
                    if nxt not in seen and nxt not in dead:
                        seen.add(nxt)
                        queue.append((nxt, steps + 1))
        return -1
