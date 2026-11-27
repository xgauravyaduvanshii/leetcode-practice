# LeetCode 2547. Minimum Cost to Split an Array — Hard
# https://leetcode.com/problems/minimum-cost-to-split-an-array/
# Submission 2201807502 — Accepted, Python3
#
# My thinking: I cut the array from the
# left, and for each new cut I stretch
# the last piece rightward, keeping a
# running count of how many of its
# numbers show up at least twice — that
# count plus k is the piece's price, and
# the cheapest cut wins.

from collections import Counter


class Solution:
    def minCost(self, nums: list[int], k: int) -> int:
        n = len(nums)
        INF = float("inf")
        dp = [INF] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            freq = Counter()
            trimmed = 0
            for j in range(i - 1, -1, -1):
                x = nums[j]
                freq[x] += 1
                if freq[x] == 2:
                    trimmed += 2
                elif freq[x] > 2:
                    trimmed += 1
                dp[i] = min(dp[i], dp[j] + k + trimmed)
        return dp[n]
