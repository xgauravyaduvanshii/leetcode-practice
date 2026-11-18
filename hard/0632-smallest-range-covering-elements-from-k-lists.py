# LeetCode 632. Smallest Range Covering Elements from K Lists — Hard
# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
# Submission 2198664813 — Accepted, Python3
#
# My thinking: a min-heap always holds one number from
# each list, so the heap's smallest value and the
# biggest value I have seen so far form a range that
# covers every list. I keep popping the smallest and
# pulling the next number from its list, shrinking the
# range whenever I can.

import heapq
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        current_max = float("-inf")
        for row, numbers in enumerate(nums):
            heapq.heappush(heap, (numbers[0], row, 0))
            current_max = max(current_max, numbers[0])
        best = [heap[0][0], current_max]
        while True:
            value, row, col = heapq.heappop(heap)
            if current_max - value < best[1] - best[0]:
                best = [value, current_max]
            if col + 1 == len(nums[row]):
                break
            nxt = nums[row][col + 1]
            heapq.heappush(heap, (nxt, row, col + 1))
            current_max = max(current_max, nxt)
        return best
