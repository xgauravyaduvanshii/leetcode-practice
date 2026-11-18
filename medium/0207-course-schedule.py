# LeetCode 207. Course Schedule — Medium
# https://leetcode.com/problems/course-schedule/
# Submission 2198448323 — Accepted, Python3
#
# My thinking: I take courses in prerequisite order
# — a course becomes takeable once all its
# prerequisites are done. I keep a count of how
# many prerequisites each course still waits on,
# start with the ones waiting on none, and free
# their followers as I go. If I manage to take
# every course there is no cycle; if I get stuck,
# there is one.

from collections import deque, defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        queue = deque([c for c in range(numCourses) if indegree[c] == 0])
        taken = 0
        while queue:
            course = queue.popleft()
            taken += 1
            for nxt in graph[course]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        return taken == numCourses
