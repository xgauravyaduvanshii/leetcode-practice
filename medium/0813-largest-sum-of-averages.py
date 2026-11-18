# LeetCode 813. Largest Sum of Averages — Medium
# https://leetcode.com/problems/largest-sum-of-averages/
# Submission 2198944378 — Accepted, Python3
#
# My thinking: with prefix sums I get any
# segment's average in one step. I build up the
# best total for one partition, then two, and so
# on — each new partition tries every place the
# last cut could go.

from typing import List


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        def average(i, j):
            return (prefix[j] - prefix[i]) / (j - i)

        dp = [0.0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = average(0, i)
        for _ in range(2, k + 1):
            new_dp = [0.0] * (n + 1)
            for j in range(1, n + 1):
                new_dp[j] = max(dp[i] + average(i, j) for i in range(j))
            dp = new_dp
        return dp[n]
