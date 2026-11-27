# LeetCode 312. Burst Balloons — Hard
# https://leetcode.com/problems/burst-balloons/
# Submission 2198403275 — Accepted, Python3
#
# My thinking: I think backwards — instead of which
# balloon pops first, I choose which pops last in
# each stretch. With the neighbours of a stretch
# fixed, the last balloon in it earns its value
# times both neighbours, and the two sides of it
# are separate smaller stretches. I add a 1 at each
# end so the edges work the same way.

from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + [n for n in nums if n > 0] + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n):
            for left in range(n - length):
                right = left + length
                for last in range(left + 1, right):
                    dp[left][right] = max(
                        dp[left][right],
                        dp[left][last] + dp[last][right] + nums[left] * nums[last] * nums[right],
                    )
        return dp[0][n - 1]
