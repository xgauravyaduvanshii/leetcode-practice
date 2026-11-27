# LeetCode 1450. Number of Students Doing Homework at a Given Time — Easy
# https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/
# Submission 2197579858 — Accepted, Python3
#
# My thinking: a student is doing homework at the
# query time exactly when that time falls between
# their start and end time. I just count how many
# intervals contain it.

class Solution:
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        count = 0
        for s, e in zip(startTime, endTime):
            if s <= queryTime <= e:
                count += 1
        return count
