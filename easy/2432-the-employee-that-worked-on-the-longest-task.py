# LeetCode 2432. The Employee That Worked on the Longest Task — Easy
# https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/
# Submission 2197783439 — Accepted, Python3
#
# My thinking: each task's duration is its end time
# minus the previous task's end time. I track the
# longest duration, and on a tie I keep the smaller
# employee id.

class Solution:
    def hardestWorker(self, n: int, logs: list[list[int]]) -> int:
        best_id = logs[0][0]
        best_time = logs[0][1]
        prev = 0
        for emp, t in logs:
            dur = t - prev
            if dur > best_time or (dur == best_time and emp < best_id):
                best_time = dur
                best_id = emp
            prev = t
        return best_id
