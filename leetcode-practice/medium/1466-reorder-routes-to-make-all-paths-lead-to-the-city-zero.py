# LeetCode 1466. Reorder Routes to Make All Paths Lead to the City Zero — Medium
# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
# Submission 2199856919 — Accepted, Python3
#
# My thinking: I walk outward from city zero.
# Every road I cross that points away from
# zero must be flipped; roads already pointing
# toward it stay as they are.

from collections import defaultdict, deque
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))
        seen = {0}
        queue = deque([0])
        changes = 0
        while queue:
            node = queue.popleft()
            for neighbor, needs_change in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    changes += needs_change
                    queue.append(neighbor)
        return changes
