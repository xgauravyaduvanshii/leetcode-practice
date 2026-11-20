# LeetCode 1760. Minimum Limit of Balls in a Bag — Medium
# https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/
# Submission 2199928766 — Accepted, Python3
#
# My thinking: for any target bag size I can
# count exactly how many splits it needs. That
# count only falls as the target grows, so I
# binary search the smallest target I can
# afford.

from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def operations_needed(limit):
            ops = 0
            for num in nums:
                ops += (num - 1) // limit
            return ops

        low, high = 1, max(nums)
        while low < high:
            mid = (low + high) // 2
            if operations_needed(mid) <= maxOperations:
                high = mid
            else:
                low = mid + 1
        return low
