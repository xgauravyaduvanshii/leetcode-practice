# LeetCode 1674. Minimum Moves to Make Array Complementary — Medium
# https://leetcode.com/problems/minimum-moves-to-make-array-complementary/
# Submission 2199907517 — Accepted, Python3
#
# My thinking: each pair costs 2 moves by
# default, 1 move for totals it can reach
# with one change, and 0 for its own sum. I
# sweep every target total with a difference
# array and keep the cheapest.

from typing import List


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0] * (2 * limit + 2)
        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]
            low = min(a, b) + 1
            high = max(a, b) + limit
            diff[2] += 2
            diff[low] -= 1
            diff[a + b] -= 1
            diff[a + b + 1] += 1
            diff[high + 1] += 1
        moves = 0
        best = n
        for total in range(2, 2 * limit + 1):
            moves += diff[total]
            best = min(best, moves)
        return best
