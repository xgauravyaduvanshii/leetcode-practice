# LeetCode 690. Employee Importance — Medium
# https://leetcode.com/problems/employee-importance/
# Submission 2198914450 — Accepted, Python3
#
# My thinking: I look up each employee by id and
# walk down through their subordinates, adding up
# the importance of everyone I reach.

from typing import List


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        by_id = {employee.id: employee for employee in employees}
        total = 0
        stack = [id]
        while stack:
            current = by_id[stack.pop()]
            total += current.importance
            stack.extend(current.subordinates)
        return total
