# LeetCode 1043. Partition Array for Maximum Sum — Medium
# https://leetcode.com/problems/partition-array-for-maximum-sum/
# Submission 2198993016 — Accepted, Python3
#
# My thinking: I work out the best total for
# every prefix. The last piece can be up to k
# long — I try each length, fill it with its
# biggest value, and add the best total before
# it.

from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            best = 0
            biggest = 0
            for j in range(1, min(k, i) + 1):
                biggest = max(biggest, arr[i - j])
                best = max(best, dp[i - j] + biggest * j)
            dp[i] = best
        return dp[n]
