# LeetCode 1819. Number of Different Subsequences GCDs — Hard
# https://leetcode.com/problems/number-of-different-subsequences-gcds/
# Submission 2201183583 — Accepted, Python3
#
# My thinking: a gcd g is reachable exactly when
# the numbers that are multiples of g have gcd g
# themselves, so I check every g up to the largest
# number.

import math

class Solution:
    def countDifferentSubsequenceGCDs(self, nums: list[int]) -> int:
        present = set(nums)
        mx = max(nums)
        ans = 0
        for g in range(1, mx + 1):
            cur = 0
            for m in range(g, mx + 1, g):
                if m in present:
                    cur = math.gcd(cur, m)
                    if cur == g:
                        break
            if cur == g:
                ans += 1
        return ans
