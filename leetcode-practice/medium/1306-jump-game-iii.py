# LeetCode 1306. Jump Game III — Medium
# https://leetcode.com/problems/jump-game-iii/
# Submission 2199028097 — Accepted, Python3
#
# My thinking: from each landing spot I can
# jump forward or back by the number written
# there. A breadth-first walk from the start
# reaches a zero exactly when the answer is yes.

from collections import deque
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        seen = {start}
        queue = deque([start])
        while queue:
            i = queue.popleft()
            if arr[i] == 0:
                return True
            for nxt in (i + arr[i], i - arr[i]):
                if 0 <= nxt < len(arr) and nxt not in seen:
                    seen.add(nxt)
                    queue.append(nxt)
        return False
