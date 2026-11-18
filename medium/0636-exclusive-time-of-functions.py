# LeetCode 636. Exclusive Time of Functions — Medium
# https://leetcode.com/problems/exclusive-time-of-functions/
# Submission 2198888728 — Accepted, Python3
#
# My thinking: a stack holds the function that is
# running right now. Each log entry closes the gap
# since the previous one — the running function
# earns the time up to a nested start, and the
# whole span up to its own end.

from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * n
        stack = []
        previous = 0
        for log in logs:
            function_id, kind, time = log.split(":")
            function_id, time = int(function_id), int(time)
            if kind == "start":
                if stack:
                    result[stack[-1]] += time - previous
                stack.append(function_id)
                previous = time
            else:
                result[stack.pop()] += time - previous + 1
                previous = time + 1
        return result
