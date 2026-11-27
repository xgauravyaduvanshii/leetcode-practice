# 1871. Jump Game VII (Medium)
# https://leetcode.com/problems/jump-game-vii/
# Submission 2199952408 — Accepted, Python3
from collections import deque


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # My thinking: walk the string with a queue of
        # reachable positions. From each one, every zero
        # inside its jump window becomes reachable too.
        # A "farthest" marker makes sure no index is ever
        # scanned twice, so the whole walk stays linear.
        n = len(s)
        if s[-1] != "0":
            return False
        queue = deque([0])
        farthest = 0
        while queue:
            i = queue.popleft()
            low = max(i + minJump, farthest + 1)
            high = min(i + maxJump, n - 1)
            for j in range(low, high + 1):
                if s[j] == "0":
                    if j == n - 1:
                        return True
                    queue.append(j)
            farthest = max(farthest, high)
        return False
