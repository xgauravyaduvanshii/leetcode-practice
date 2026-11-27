# LeetCode 1536. Minimum Swaps to Arrange a Binary Grid — Medium
# https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/
# Submission 2199870993 — Accepted, Python3
#
# My thinking: each row only matters by how
# many trailing zeros it has. Row i needs
# n - 1 - i of them, so I greedily pull the
# nearest row below that qualifies and count
# the swaps to bring it up.

from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        zeros = []
        for row in grid:
            count = 0
            for value in reversed(row):
                if value == 0:
                    count += 1
                else:
                    break
            zeros.append(count)
        swaps = 0
        for i in range(n):
            need = n - 1 - i
            j = i
            while j < n and zeros[j] < need:
                j += 1
            if j == n:
                return -1
            while j > i:
                zeros[j], zeros[j - 1] = zeros[j - 1], zeros[j]
                swaps += 1
                j -= 1
        return swaps
