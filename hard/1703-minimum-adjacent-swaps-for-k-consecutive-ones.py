# LeetCode 1703. Minimum Adjacent Swaps for K Consecutive Ones — Hard
# https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/
# Submission 2201100269 — Accepted, Python3
#
# My thinking: only the ones matter, so I list their
# positions and slide a window of k across them — for
# each window I count how far every one has to travel
# to sit next to the middle one, using prefix sums to
# keep it fast.

class Solution:
    def minMoves(self, nums: list[int], k: int) -> int:
        ones = [i for i, v in enumerate(nums) if v == 1]
        # q[i] = ones[i] - i turns the cost into a plain
        # distance-to-median problem.
        q = [pos - i for i, pos in enumerate(ones)]
        prefix = [0] * (len(q) + 1)
        for i, v in enumerate(q):
            prefix[i + 1] = prefix[i] + v
        best = float("inf")
        for i in range(len(q) - k + 1):
            mid = i + k // 2
            median = q[mid]
            left = median * (mid - i) - (prefix[mid] - prefix[i])
            right = (prefix[i + k] - prefix[mid + 1]) - median * (i + k - mid - 1)
            best = min(best, left + right)
        return best
