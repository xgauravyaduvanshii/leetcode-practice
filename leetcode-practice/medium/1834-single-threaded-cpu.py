# LeetCode 1834. Single-Threaded CPU — Medium
# https://leetcode.com/problems/single-threaded-cpu/
# Submission 2199945492 — Accepted, Python3
#
# My thinking: tasks wait in a heap ordered
# by processing time, then by index. The
# clock jumps to the next arrival when the
# heap is empty, and each task runs to
# completion once started.

import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        indexed = sorted((enqueue, process, i) for i, (enqueue, process) in enumerate(tasks))
        available = []
        result = []
        time = 0
        i = 0
        while i < len(indexed) or available:
            if not available:
                time = max(time, indexed[i][0])
            while i < len(indexed) and indexed[i][0] <= time:
                enqueue, process, idx = indexed[i]
                heapq.heappush(available, (process, idx))
                i += 1
            process, idx = heapq.heappop(available)
            time += process
            result.append(idx)
        return result
