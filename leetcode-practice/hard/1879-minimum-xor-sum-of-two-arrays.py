# LeetCode 1879. Minimum XOR Sum of Two Arrays — Hard
# https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/
# Submission 2201214115 — Accepted, Python3
#
# My thinking: I assign the second array to the
# first one element at a time and keep, for every
# set of already-used positions, the cheapest xor
# sum so far — a bitmask holds which positions
# are taken.

class Solution:
    def minimumXORSum(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        INF = float("inf")
        dp = [INF] * (1 << n)
        dp[0] = 0
        for mask in range(1 << n):
            i = bin(mask).count("1")
            if i >= n:
                continue
            for j in range(n):
                if not (mask >> j) & 1:
                    dp[mask | (1 << j)] = min(dp[mask | (1 << j)], dp[mask] + (nums1[i] ^ nums2[j]))
        return dp[(1 << n) - 1]
