# LeetCode 3321. Find X-Sum of All K-Long Subarrays II — Hard
# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/
# Submission 2202369662 — Accepted, Python3
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        # My thinking: in each window I keep the x most frequent distinct
        # values (ties broken by the bigger value) in a "top" set and the
        # rest in a "rest" set, with the x-sum maintained incrementally.
        # Both sets are heaps with lazy deletion: top is a min-heap keyed by
        # (frequency, value) so its worst element is on top, rest is a
        # max-heap on the same key. When a value's frequency changes I evict
        # it from top if it is there, push the fresh entry into rest, and
        # rebalance — refill top from rest, swap whenever the best of rest
        # beats the worst of top, and shrink top back to x.
        freq = defaultdict(int)
        top = []   # min-heap of (frequency, value)
        rest = []  # min-heap of (-frequency, -value)
        in_top = {}
        top_cnt = 0
        top_sum = 0

        def clean_top():
            while top:
                f, v = top[0]
                if freq.get(v, 0) == f and in_top.get(v, False):
                    return
                heapq.heappop(top)

        def clean_rest():
            while rest:
                f, v = -rest[0][0], -rest[0][1]
                if freq.get(v, 0) == f and not in_top.get(v, False):
                    return
                heapq.heappop(rest)

        def rebalance():
            nonlocal top_cnt, top_sum
            clean_top()
            clean_rest()
            while top_cnt < x:
                clean_rest()
                if not rest:
                    break
                f, v = -rest[0][0], -rest[0][1]
                heapq.heappop(rest)
                in_top[v] = True
                top_cnt += 1
                top_sum += f * v
                heapq.heappush(top, (f, v))
            while True:
                clean_top()
                clean_rest()
                if not top or not rest:
                    break
                f1, v1 = top[0]
                f2, v2 = -rest[0][0], -rest[0][1]
                if (f2, v2) > (f1, v1):
                    heapq.heappop(top)
                    heapq.heappop(rest)
                    in_top[v1] = False
                    in_top[v2] = True
                    top_sum += f2 * v2 - f1 * v1
                    heapq.heappush(top, (f2, v2))
                    heapq.heappush(rest, (-f1, -v1))
                else:
                    break
            while top_cnt > x:
                clean_top()
                f, v = heapq.heappop(top)
                in_top[v] = False
                top_cnt -= 1
                top_sum -= f * v
                heapq.heappush(rest, (-f, -v))

        def change(v: int, delta: int):
            nonlocal top_cnt, top_sum
            old = freq.get(v, 0)
            if in_top.get(v, False):
                top_sum -= old * v
                top_cnt -= 1
                in_top[v] = False
            new = old + delta
            if new > 0:
                freq[v] = new
                heapq.heappush(rest, (-new, -v))
            else:
                freq.pop(v, None)
            rebalance()

        ans = []
        for i, v in enumerate(nums):
            change(v, 1)
            if i >= k:
                change(nums[i - k], -1)
            if i >= k - 1:
                ans.append(top_sum)
        return ans
