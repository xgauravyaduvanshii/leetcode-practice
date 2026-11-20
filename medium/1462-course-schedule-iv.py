# LeetCode 1462. Course Schedule IV — Medium
# https://leetcode.com/problems/course-schedule-iv/
# Submission 2199854826 — Accepted, Python3
#
# My thinking: I build a reachability table —
# course a reaches course b directly or through
# a middle course — then every query is one
# lookup in that table.

from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        reach = [[False] * numCourses for _ in range(numCourses)]
        for a, b in prerequisites:
            reach[a][b] = True
        for mid in range(numCourses):
            for start in range(numCourses):
                if reach[start][mid]:
                    for end in range(numCourses):
                        if reach[mid][end]:
                            reach[start][end] = True
        return [reach[a][b] for a, b in queries]
