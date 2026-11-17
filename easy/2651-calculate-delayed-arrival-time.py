# LeetCode 2651. Calculate Delayed Arrival Time — Easy
# https://leetcode.com/problems/calculate-delayed-arrival-time/
# Submission 2197811530 — Accepted, Python3
#
# My thinking: the arrival time is just the sum of
# the two times, wrapped around a 24-hour clock.

class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime) % 24
