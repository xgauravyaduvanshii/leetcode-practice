# LeetCode 3510. Minimum Pair Removal to Sort Array II — Hard
# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/
# Submission 2202767694 — Accepted, Python3
import heapq
from typing import List


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        # My thinking: the process is forced — always merge the
        # adjacent pair with the smallest sum, leftmost on a tie — so I
        # just simulate it. A doubly linked list holds the live array
        # and a heap holds every adjacent pair by (sum, left index);
        # stale heap entries are skipped by checking that both ends are
        # still alive and still neighbours. I count how many adjacent
        # pairs are out of order and stop as soon as that count hits
        # zero, updating it only around the merged pair.
        n = len(nums)
        if n <= 1:
            return 0
        val = list(nums)
        left = [i - 1 for i in range(n)]
        right = [i + 1 for i in range(n)]
        right[n - 1] = -1
        alive = [True] * n
        bad = sum(1 for i in range(n - 1) if nums[i] > nums[i + 1])
        heap = []
        for i in range(n - 1):
            heapq.heappush(heap, (nums[i] + nums[i + 1], i))
        ops = 0
        while bad > 0:
            while True:
                ssum, i = heapq.heappop(heap)
                if not alive[i]:
                    continue
                j = right[i]
                if j == -1 or not alive[j]:
                    continue
                if val[i] + val[j] != ssum:
                    continue
                break
            j = right[i]
            L = left[i]
            R = right[j]

            def is_descent(a, b):
                return a != -1 and b != -1 and alive[a] and alive[b] and val[a] > val[b]

            if is_descent(L, i):
                bad -= 1
            if is_descent(i, j):
                bad -= 1
            if is_descent(j, R):
                bad -= 1
            val[i] = val[i] + val[j]
            alive[j] = False
            right[i] = R
            if R != -1:
                left[R] = i
            if is_descent(L, i):
                bad += 1
            if is_descent(i, R):
                bad += 1
            if L != -1:
                heapq.heappush(heap, (val[L] + val[i], L))
            if R != -1:
                heapq.heappush(heap, (val[i] + val[R], i))
            ops += 1
        return ops
