# LeetCode 2001. Number of Pairs of Interchangeable Rectangles — Medium
# https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/
# Submission 2204121734 — Accepted, Python3
#
# My thinking: two rectangles are interchangeable when their
# width-to-height ratios are equal, so I reduce each ratio to its
# simplest form by dividing both sides by their greatest common
# divisor and count how many rectangles share each reduced ratio.
# From a group of n rectangles with the same ratio, I can form
# n * (n - 1) / 2 pairs, and I add that up over all groups.
from math import gcd
from collections import Counter


class Solution:
    def interchangeableRectangles(self, rectangles):
        counts = Counter()
        for width, height in rectangles:
            divisor = gcd(width, height)
            counts[(width // divisor, height // divisor)] += 1
        pairs = 0
        for count in counts.values():
            pairs += count * (count - 1) // 2
        return pairs


if __name__ == "__main__":
    solution = Solution()
    # Example 1
    assert solution.interchangeableRectangles(
        [[4, 8], [3, 6], [10, 20], [15, 30]]) == 6
    # Example 2
    assert solution.interchangeableRectangles([[4, 5], [7, 8]]) == 0
    # Extra checks: mixed ratios, single rectangle
    assert solution.interchangeableRectangles(
        [[2, 4], [1, 2], [3, 5], [6, 10]]) == 2
    assert solution.interchangeableRectangles([[1, 1]]) == 0
    print("All sample tests passed.")
