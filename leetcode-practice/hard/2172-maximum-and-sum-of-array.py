# LeetCode 2172. Maximum AND Sum of Array — Hard
# https://leetcode.com/problems/maximum-and-sum-of-array/
# Submission 2201600458 — Accepted, Python3
#
# My thinking: each slot holds two numbers,
# so a slot is two switches — I walk through
# the subsets of switches, put the next
# number in every free one, and keep the
# best sum that fills every number.

class Solution:
    def maximumANDSum(self, nums: list[int], numSlots: int) -> int:
        m = 2 * numSlots
        size = 1 << m
        dp = [-1] * size
        dp[0] = 0
        ans = 0
        for mask in range(size):
            if dp[mask] < 0:
                continue
            used = bin(mask).count('1')
            if used == len(nums):
                ans = max(ans, dp[mask])
                continue
            for b in range(m):
                if mask >> b & 1:
                    continue
                nxt = mask | (1 << b)
                val = dp[mask] + (nums[used] & (b // 2 + 1))
                if val > dp[nxt]:
                    dp[nxt] = val
        return ans
