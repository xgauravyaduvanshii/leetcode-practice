# LeetCode 1144. Decrease Elements To Make Array Zigzag — Medium
# https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/
# Submission 2199005087 — Accepted, Python3
#
# My thinking: either the even spots are the
# peaks or the odd spots are. For each choice I
# lower every peak to just below its smaller
# neighbour and add up what that costs.

from typing import List


class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        def cost(even_peaks):
            total = 0
            for i, value in enumerate(nums):
                if (i % 2 == 0) == even_peaks:
                    need = value
                    if i > 0:
                        need = min(need, nums[i - 1] - 1)
                    if i < len(nums) - 1:
                        need = min(need, nums[i + 1] - 1)
                    total += max(0, value - need)
            return total

        return min(cost(True), cost(False))
