# LeetCode 2365. Task Scheduler II — Medium
# https://leetcode.com/problems/task-scheduler-ii/
# Submission 2204748423 — Accepted, Python3
#
# My thinking: track the last day each task type ran. A task can run on
# the current day, unless its previous run was fewer than `space` days
# ago — then I must wait until last + space + 1. Each task takes one
# day, so after placing it I move to the next day. The final day count
# is the answer.
class Solution:
    def taskSchedulerII(self, tasks: list[int], space: int) -> int:
        last = {}
        day = 0
        for t in tasks:
            if t in last:
                day = max(day, last[t] + space + 1)
            last[t] = day
            day += 1
        return day
