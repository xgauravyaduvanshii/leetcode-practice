# LeetCode 2059. Minimum Operations to Convert Number — Medium
# https://leetcode.com/problems/minimum-operations-to-convert-number/
# Submission 2204389857 — Accepted, Python3
#
# My thinking: this is a shortest path in the space of reachable
# values, so I run BFS from start. From each value I can add, subtract
# or XOR any of the given numbers; values outside 0..1000 are only
# useful if they equal the goal, so I never enqueue them. The first
# time I reach the goal, the BFS depth is the minimum number of
# operations; exhausting the queue means it is unreachable.
from collections import deque


class Solution:
    def minimumOperations(self, nums: list[int], start: int, goal: int) -> int:
        q = deque([start])
        seen = {start}
        steps = 0
        while q:
            for _ in range(len(q)):
                v = q.popleft()
                if v == goal:
                    return steps
                for x in nums:
                    for nv in (v + x, v - x, v ^ x):
                        if nv == goal:
                            return steps + 1
                        if 0 <= nv <= 1000 and nv not in seen:
                            seen.add(nv)
                            q.append(nv)
            steps += 1
        return -1
