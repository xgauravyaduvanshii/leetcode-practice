# LeetCode 1701. Average Waiting Time — Medium
# https://leetcode.com/problems/average-waiting-time/
# Submission 2199914828 — Accepted, Python3
#
# My thinking: the chef starts each order
# when he is free or the customer arrives,
# whichever is later. I add up every
# customer's wait and divide by the count.

from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        free_at = 0
        total_wait = 0
        for arrival, time in customers:
            start = max(free_at, arrival)
            free_at = start + time
            total_wait += free_at - arrival
        return total_wait / len(customers)
