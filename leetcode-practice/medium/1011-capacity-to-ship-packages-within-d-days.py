# LeetCode 1011. Capacity To Ship Packages Within D Days — Medium
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
# Submission 2198986308 — Accepted, Python3
#
# My thinking: the smallest working capacity lies
# between the heaviest single package and the
# total weight. I binary search that range,
# counting how many days each trial capacity
# needs.

from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def days_needed(capacity):
            needed = 1
            load = 0
            for weight in weights:
                if load + weight > capacity:
                    needed += 1
                    load = 0
                load += weight
            return needed

        low, high = max(weights), sum(weights)
        while low < high:
            mid = (low + high) // 2
            if days_needed(mid) <= days:
                high = mid
            else:
                low = mid + 1
        return low
