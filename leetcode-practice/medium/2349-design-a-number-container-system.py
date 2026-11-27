# LeetCode 2349. Design a Number Container System — Medium
# https://leetcode.com/problems/design-a-number-container-system/
# Submission 2204728642 — Accepted, Python3
#
# My thinking: keep an index->number map, plus one min-heap of indices
# per number. change() records the new number and pushes the index onto
# that number's heap (old entries stay, they are stale). find() lazily
# pops stale heap tops — entries whose index now holds a different
# number — until the top is fresh, then returns the smallest index, or
# -1 when the heap is empty.
import heapq

class NumberContainers:
    def __init__(self):
        self.index_to_num = {}
        self.num_to_heap = {}

    def change(self, index: int, number: int) -> None:
        self.index_to_num[index] = number
        if number not in self.num_to_heap:
            self.num_to_heap[number] = []
        heapq.heappush(self.num_to_heap[number], index)

    def find(self, number: int) -> int:
        heap = self.num_to_heap.get(number)
        if not heap:
            return -1
        while heap and self.index_to_num.get(heap[0]) != number:
            heapq.heappop(heap)
        return heap[0] if heap else -1
