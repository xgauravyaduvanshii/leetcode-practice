# LeetCode 1577. Number of Ways Where Square of Number Is Equal to Product of Two Numbers — Medium
# https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/
# Submission 2199883690 — Accepted, Python3
#
# My thinking: a triplet needs one square
# from one array matching a pair product from
# the other. I count all squares and all pair
# products, then match them up — in both
# directions.

from collections import Counter
from typing import List


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def count(a, b):
            squares = Counter(x * x for x in a)
            pairs = Counter()
            for i in range(len(b)):
                for j in range(i + 1, len(b)):
                    pairs[b[i] * b[j]] += 1
            return sum(count * pairs[square] for square, count in squares.items())

        return count(nums1, nums2) + count(nums2, nums1)
