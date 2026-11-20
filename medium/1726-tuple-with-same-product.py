# LeetCode 1726. Tuple with Same Product — Medium
# https://leetcode.com/problems/tuple-with-same-product/
# Submission 2199921546 — Accepted, Python3
#
# My thinking: two pairs with the same product
# make eight tuples — each pair can lead or
# follow, and each can flip. I count the pairs
# per product and combine them.

from collections import Counter
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        products = Counter()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                products[nums[i] * nums[j]] += 1
        return sum(count * (count - 1) // 2 * 8 for count in products.values())
