# LeetCode 480. Sliding Window Median — Hard
# https://leetcode.com/problems/sliding-window-median/
# Submission 2198660214 — Accepted, Python3
#
# My thinking: two heaps hold the window — the lower
# half as a max-heap, the upper half as a min-heap.
# Each entry carries its index, so when a value slides
# out of the window it is only dropped from the heap
# it actually sits in; a plain value-based cleanup
# would prune a duplicate from the wrong heap.

import heapq
from collections import defaultdict
from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        small = []  # max-heap of (-value, index)
        large = []  # min-heap of (value, index)
        delayed = defaultdict(int)
        small_count = 0
        large_count = 0

        def prune(heap):
            while heap:
                value, index = heap[0]
                if delayed[index]:
                    delayed[index] -= 1
                    heapq.heappop(heap)
                else:
                    break

        def balance():
            nonlocal small_count, large_count
            if small_count > large_count + 1:
                value, index = heapq.heappop(small)
                heapq.heappush(large, (-value, index))
                small_count -= 1
                large_count += 1
                prune(small)
            elif small_count < large_count:
                value, index = heapq.heappop(large)
                heapq.heappush(small, (-value, index))
                large_count -= 1
                small_count += 1
                prune(large)

        answers = []
        for i, num in enumerate(nums):
            if not small or num <= -small[0][0]:
                heapq.heappush(small, (-num, i))
                small_count += 1
            else:
                heapq.heappush(large, (num, i))
                large_count += 1
            balance()

            if i >= k - 1:
                prune(small)
                prune(large)
                if k % 2 == 1:
                    answers.append(float(-small[0][0]))
                else:
                    answers.append((-small[0][0] + large[0][0]) / 2)
                delayed[i - k + 1] += 1
                if nums[i - k + 1] <= -small[0][0]:
                    small_count -= 1
                else:
                    large_count -= 1
                prune(small)
                prune(large)
                balance()
        return answers
