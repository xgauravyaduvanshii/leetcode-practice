# LeetCode 1962. Remove Stones to Minimize the Total — Medium
# https://leetcode.com/problems/remove-stones-to-minimize-the-total/
# Submission 2204260458 — Accepted, Python3
#
# My thinking: each operation should hit the biggest pile, because
# removing floor(pile / 2) stones from it takes away the most stones
# possible in one move, and making a big pile smaller never hurts a
# later move. A max-heap (stored as negatives, since Python's heap
# is a min-heap) always hands me the biggest pile: I pop it, cut it
# down to pile minus pile // 2, and push it back. After k operations
# the heap holds the final piles, and their sum is the answer.
import heapq


class Solution:
    def minStoneSum(self, piles, k):
        heap = [-p for p in piles]
        heapq.heapify(heap)
        for _ in range(k):
            biggest = -heapq.heappop(heap)
            biggest -= biggest // 2
            heapq.heappush(heap, -biggest)
        return -sum(heap)
