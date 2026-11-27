# LeetCode 2518. Number of Great Partitions — Hard
# https://leetcode.com/problems/number-of-great-partitions/
# Submission 2201794790 — Accepted, Python3
#
# My thinking: a partition fails when
# either side falls short of k, so I
# count the subsets that fall short —
# each one spoils two orderings — and
# take them away from every possible
# split of the array.

class Solution:
    def countPartitions(self, nums: list[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        if sum(nums) < 2 * k:
            return 0
        dp = [0] * k
        dp[0] = 1
        for x in nums:
            for s in range(k - 1, -1, -1):
                if s + x < k:
                    dp[s + x] = (dp[s + x] + dp[s]) % MOD
        bad = sum(dp) % MOD
        return (pow(2, len(nums), MOD) - 2 * bad) % MOD
