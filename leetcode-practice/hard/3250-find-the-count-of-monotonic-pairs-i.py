# LeetCode 3250. Find the Count of Monotonic Pairs I — Hard
# https://leetcode.com/problems/find-the-count-of-monotonic-pairs-i/
# Submission 2202136765 — Accepted, Python3
#
# My thinking: split each nums[i] into arr1[i]
# + arr2[i] with arr1 non-decreasing and arr2
# non-increasing. I keep a DP over the value of
# arr1[i]; moving to the next number, arr1 must
# grow by at least max(0, nums[i] - nums[i-1])
# to keep arr2 non-increasing, and a prefix sum
# makes each transition O(1).

from typing import List


class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        max_v = max(nums)
        dp = [1] * (nums[0] + 1)
        for i in range(1, len(nums)):
            d = nums[i] - nums[i - 1]
            need = d if d > 0 else 0
            pref = [0] * (len(dp) + 1)
            for t in range(len(dp)):
                pref[t + 1] = (pref[t] + dp[t]) % MOD
            ndp = [0] * (nums[i] + 1)
            for s in range(nums[i] + 1):
                lim = s - need
                if lim >= 0:
                    if lim >= len(dp):
                        lim = len(dp) - 1
                    ndp[s] = pref[lim + 1]
            dp = ndp
        return sum(dp) % MOD
