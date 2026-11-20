# LeetCode 1802. Maximum Value at a Given Index in a Bounded Array — Medium
# https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/
# Submission 2199939421 — Accepted, Python3
#
# My thinking: a peak of some height forces
# a mountain shape on both sides, so I can
# add up exactly what it costs. The cost
# only grows with the height, so I binary
# search the tallest peak the budget allows.

class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def side_sum(count, peak):
            if count == 0:
                return 0
            if peak - 1 >= count:
                return (peak - 1 + peak - count) * count // 2
            return peak * (peak - 1) // 2 + (count - peak + 1)

        def total(peak):
            return peak + side_sum(index, peak) + side_sum(n - index - 1, peak)

        low, high = 1, maxSum
        while low < high:
            mid = (low + high + 1) // 2
            if total(mid) <= maxSum:
                low = mid
            else:
                high = mid - 1
        return low
