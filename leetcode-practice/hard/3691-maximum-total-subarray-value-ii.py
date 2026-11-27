# LeetCode 3691. Maximum Total Subarray Value II — Hard
# https://leetcode.com/problems/maximum-total-subarray-value-ii/
# Submission 2203042569 — Accepted, Python3
from collections import deque
from typing import List


def _count_ge(nums: List[int], t: int) -> int:
    # My thinking: for a fixed right end, max - min only grows
    # as the left end moves left, so the left ends with value
    # >= t form a prefix [0..left-1]. A sliding window with
    # monotone deques finds that prefix for every right end in
    # linear time, and the prefix lengths add up to the count.
    n = len(nums)
    maxd: deque = deque()
    mind: deque = deque()
    left = 0
    total = 0
    for r in range(n):
        while maxd and nums[maxd[-1]] <= nums[r]:
            maxd.pop()
        maxd.append(r)
        while mind and nums[mind[-1]] >= nums[r]:
            mind.pop()
        mind.append(r)
        while left <= r and nums[maxd[0]] - nums[mind[0]] >= t:
            left += 1
            while maxd and maxd[0] < left:
                maxd.popleft()
            while mind and mind[0] < left:
                mind.popleft()
        total += left
    return total


def _thresholds(nums: List[int], t: int) -> List[int]:
    # My thinking: same sliding window as _count_ge, but instead
    # of adding up the counts I keep, for each right end r, the
    # largest left end L with value >= t (or -1 when there is
    # none) — those are exactly the left ends whose subarrays
    # ending at r count towards the sum above the threshold.
    n = len(nums)
    maxd: deque = deque()
    mind: deque = deque()
    left = 0
    out = []
    for r in range(n):
        while maxd and nums[maxd[-1]] <= nums[r]:
            maxd.pop()
        maxd.append(r)
        while mind and nums[mind[-1]] >= nums[r]:
            mind.pop()
        mind.append(r)
        while left <= r and nums[maxd[0]] - nums[mind[0]] >= t:
            left += 1
            while maxd and maxd[0] < left:
                maxd.popleft()
            while mind and mind[0] < left:
                mind.popleft()
        out.append(left - 1)
    return out


class _Extremes:
    # My thinking: for a fixed right end, the max (or min) over
    # [l..r] only changes at a few left ends, so I keep the
    # segments in a stack, each with its value, its rightmost
    # index, and the running sum up to that index. Appending a
    # new right end pops every segment the new value dominates
    # and merges them into one, so a prefix sum over [0..L] is
    # a binary search plus one multiplication.
    def __init__(self, is_max: bool):
        self.is_max = is_max
        self.nodes = []

    def append(self, r: int, v: int) -> None:
        nodes = self.nodes
        total = 1
        while nodes:
            val, right, _pref = nodes[-1]
            if (self.is_max and val <= v) or (not self.is_max and val >= v):
                prev_right = nodes[-2][1] if len(nodes) >= 2 else -1
                total += right - prev_right
                nodes.pop()
            else:
                break
        base = nodes[-1][2] if nodes else 0
        nodes.append([v, r, base + v * total])

    def prefix_sum(self, left: int) -> int:
        if left < 0:
            return 0
        nodes = self.nodes
        lo, hi = 0, len(nodes) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nodes[mid][1] < left:
                lo = mid + 1
            else:
                hi = mid
        val, _right, _pref = nodes[lo]
        prev_right = nodes[lo - 1][1] if lo > 0 else -1
        prev_pref = nodes[lo - 1][2] if lo > 0 else 0
        return prev_pref + val * (left - prev_right)


class Solution:
    def maxTotalSubarrayValue(self, nums: List[int], k: int) -> int:
        # My thinking: the k-th largest subarray value T* is
        # found by binary searching the threshold, since the
        # count of subarrays with value >= t falls as t rises.
        # Every subarray worth more than T* must be added in
        # full, and the rest of the k picks are all exactly T*.
        # The full sum comes from the segment stacks: for each
        # right end I add the sum of maxes minus the sum of
        # mins over exactly the left ends above the threshold.
        hi = max(nums) - min(nums)
        lo, hi2 = 0, hi
        while lo < hi2:
            mid = (lo + hi2 + 1) // 2
            if _count_ge(nums, mid) >= k:
                lo = mid
            else:
                hi2 = mid - 1
        t_star = lo
        count_gt = _count_ge(nums, t_star + 1)
        limits = _thresholds(nums, t_star + 1)
        mx = _Extremes(True)
        mn = _Extremes(False)
        sum_gt = 0
        for r, v in enumerate(nums):
            mx.append(r, v)
            mn.append(r, v)
            if limits[r] >= 0:
                sum_gt += mx.prefix_sum(limits[r]) - mn.prefix_sum(limits[r])
        return sum_gt + (k - count_gt) * t_star
