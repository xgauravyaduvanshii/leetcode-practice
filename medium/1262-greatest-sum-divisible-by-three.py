# LeetCode 1262. Greatest Sum Divisible by Three — Medium
# https://leetcode.com/problems/greatest-sum-divisible-by-three/
# Submission 2199021589 — Accepted, Python3
#
# My thinking: I track the best sum for each
# remainder when divided by three. Each number
# either joins a sum and shifts its remainder,
# or is skipped — and the best remainder-zero
# sum is the answer.

from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, float("-inf"), float("-inf")]
        for value in nums:
            nxt = dp[:]
            for remainder in range(3):
                nxt[(remainder + value) % 3] = max(nxt[(remainder + value) % 3], dp[remainder] + value)
            dp = nxt
        return dp[0]
