# LeetCode 2050. Parallel Courses III — Hard
# https://leetcode.com/problems/parallel-courses-iii/
# Submission 2201562170 — Accepted, Python3
#
# My thinking: a course can only start once its
# slowest prerequisite is done, so I walk the
# courses in prerequisite order and each one
# finishes at its own time plus the slowest
# prerequisite — the last finish is the answer.

from collections import deque


class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        graph = [[] for _ in range(n + 1)]
        indeg = [0] * (n + 1)
        for u, v in relations:
            graph[u].append(v)
            indeg[v] += 1
        finish = [0] * (n + 1)
        q = deque()
        for i in range(1, n + 1):
            if indeg[i] == 0:
                q.append(i)
                finish[i] = time[i - 1]
        while q:
            u = q.popleft()
            for v in graph[u]:
                finish[v] = max(finish[v], finish[u] + time[v - 1])
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        return max(finish)
