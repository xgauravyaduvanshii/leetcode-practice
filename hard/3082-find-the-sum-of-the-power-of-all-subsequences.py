# LeetCode 3082. Find the Sum of the Power of All Subsequences — Hard
# https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences/
# Submission 2201926404 — Accepted, Python3
#
# My thinking: instead of counting
# inside every subsequence, I count by
# the inner one. A set T that sums to k
# sits inside exactly 2^(n - |T|)
# subsequences — every other element is
# freely in or out — so the answer is
# the sum of 2^(n - |T|) over all such
# sets T. I count those sets by sum and
# size with a small knapsack DP.

from typing import List

MOD = 1_000_000_007


class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # dp[s][c]: sets with sum s and c elements.
        dp = [[0] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 1
        for x in nums:
            for s in range(k, x - 1, -1):
                for c in range(n, 0, -1):
                    dp[s][c] = (dp[s][c] + dp[s - x][c - 1]) % MOD
        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = pow2[i - 1] * 2 % MOD
        ans = 0
        for c in range(n + 1):
            ans = (ans + dp[k][c] * pow2[n - c]) % MOD
        return ans
