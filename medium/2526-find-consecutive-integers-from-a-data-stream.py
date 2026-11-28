# LeetCode 2526. Find Consecutive Integers from a Data Stream — Medium
# https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/
# Submission 2205049750 — Accepted, Python3
#
# My thinking: only the current run of the target value matters, so
# keep one counter: bump it when the incoming number equals value,
# reset it to zero otherwise. consec is true exactly when the run
# has reached k.
class DataStream:
    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.run = 0

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.run += 1
        else:
            self.run = 0
        return self.run >= self.k
