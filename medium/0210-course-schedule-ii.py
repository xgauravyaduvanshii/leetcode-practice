# LeetCode 210. Course Schedule II — Medium
# https://leetcode.com/problems/course-schedule-ii/
# Submission 2198451355 — Accepted, Python3
#
# My thinking: same walk as Course Schedule, but
# this time I write down the order I take the
# courses in — a course becomes takeable once all
# its prerequisites are done. If I take every
# course, that order respects all the prerequisites;
# if I get stuck partway, a cycle makes it
# impossible and the answer is empty.

from collections import deque, defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        queue = deque([c for c in range(numCourses) if indegree[c] == 0])
        order = []
        while queue:
            course = queue.popleft()
            order.append(course)
            for nxt in graph[course]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        return order if len(order) == numCourses else []
