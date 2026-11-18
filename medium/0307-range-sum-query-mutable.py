# LeetCode 307. Range Sum Query - Mutable — Medium
# https://leetcode.com/problems/range-sum-query-mutable/
# Submission 2198737839 — Accepted, Python3
#
# My thinking: a Fenwick tree keeps partial sums in
# a way that both updating one value and adding up a
# prefix take logarithmic time. A range sum is then
# just two prefix sums subtracted.

from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.tree = [0] * (len(nums) + 1)
        for i, value in enumerate(nums):
            self._add(i + 1, value)

    def _add(self, index: int, delta: int) -> None:
        while index < len(self.tree):
            self.tree[index] += delta
            index += index & -index

    def _prefix(self, index: int) -> int:
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total

    def update(self, index: int, val: int) -> None:
        self._add(index + 1, val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self._prefix(right + 1) - self._prefix(left)
