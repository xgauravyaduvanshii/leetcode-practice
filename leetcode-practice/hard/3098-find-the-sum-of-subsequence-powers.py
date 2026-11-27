# LeetCode 3098. Find the Sum of Subsequence Powers — Hard
# https://leetcode.com/problems/find-the-sum-of-subsequence-powers/
# Submission 2201989527 — Accepted, Python3
#
# My thinking: after sorting, a
# subsequence's power is the smallest
# gap between consecutive elements. For
# a candidate gap d I count the
# subsequences of size k whose gaps are
# all at least d, with a DP over the
# sorted numbers (bisect finds the last
# element far enough back). Counting
# this for every distinct gap and adding
# (d - previous d) times the count gives
# the sum over all subsequences.

from bisect import bisect_right
from typing import List


class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()
        n = len(nums)
        diffs = set()
        for i in range(n):
            for j in range(i + 1, n):
                d = nums[j] - nums[i]
                if d > 0:
                    diffs.add(d)
        if not diffs:
            return 0
        diffs = sorted(diffs)

        def count_ge(d):
            limits = [bisect_right(nums, nums[i] - d, 0, i) - 1 for i in range(n)]
            dp = [1] * n
            for _length in range(2, k + 1):
                pref = []
                s = 0
                for v in dp:
                    s = (s + v) % MOD
                    pref.append(s)
                dp = [pref[p] if p >= 0 else 0 for p in limits]
                if not any(dp):
                    return 0
            return sum(dp) % MOD

        ans = 0
        prev = 0
        for d in diffs:
            c = count_ge(d)
            if c:
                ans = (ans + (d - prev) * c) % MOD
            prev = d
        return ans
