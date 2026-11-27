# LeetCode 2163. Minimum Difference in Sums After Removal of Elements — Hard
# https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/
# Submission 2201595962 — Accepted, Python3
#
# My thinking: the first half wants the
# smallest numbers it can reach and the second
# half wants the largest, so I sweep the split
# point across the middle — a heap keeps the n
# smallest on the left and the n largest on
# the right, and the best split wins.

import heapq


class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        n = len(nums) // 3
        # Smallest-sum of n elements among the first i (i from n to 2n).
        left_sum = [0] * (2 * n + 1)
        max_heap = [-x for x in nums[:n]]
        heapq.heapify(max_heap)
        total = sum(nums[:n])
        left_sum[n] = total
        for i in range(n, 2 * n):
            heapq.heappush(max_heap, -nums[i])
            total += nums[i]
            total += heapq.heappop(max_heap)
            left_sum[i + 1] = total
        # Largest-sum of n elements among the last 3n - i (i from 2n down to n).
        right_sum = [0] * (2 * n + 1)
        min_heap = nums[2 * n:]
        heapq.heapify(min_heap)
        total = sum(nums[2 * n:])
        right_sum[2 * n] = total
        for i in range(2 * n - 1, n - 1, -1):
            heapq.heappush(min_heap, nums[i])
            total += nums[i]
            total -= heapq.heappop(min_heap)
            right_sum[i] = total
        return min(left_sum[i] - right_sum[i] for i in range(n, 2 * n + 1))
