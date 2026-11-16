# LeetCode 303. Range Sum Query - Immutable — Easy
# https://leetcode.com/problems/range-sum-query-immutable/
# Submission 2197463017 — Accepted, Python3
#
# My thinking: the array never changes, so I do the
# work once up front — a prefix sum where each entry
# holds the total of everything before it. Then any
# range sum is just two lookups and one subtraction.

class NumArray:
    def __init__(self, nums: list[int]):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]
