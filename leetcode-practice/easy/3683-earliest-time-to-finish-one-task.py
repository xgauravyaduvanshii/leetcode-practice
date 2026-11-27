# 3683. Earliest Time to Finish One Task (Easy)
# https://leetcode.com/problems/earliest-time-to-finish-one-task/
# Submission 2200042966 — Accepted, Python3
from typing import List


class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        # My thinking: each task finishes at its start
        # plus its duration. The earliest finish among
        # all the tasks is the answer.
        return min(start + duration for start, duration in tasks)
