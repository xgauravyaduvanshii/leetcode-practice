# LeetCode 3351. Sum of Good Subsequences — Hard
# https://leetcode.com/problems/sum-of-good-subsequences/
# Submission 2202411538 — Accepted, Python3
from typing import List

MOD = 10 ** 9 + 7


class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        # My thinking: for each value v I keep the count of good
        # subsequences ending in v and the sum of their elements. A new
        # element x starts the singleton [x] and extends every good
        # subsequence ending in x-1 or x+1, adding x to each extended sum.
        # Neighbours differ from x, so updating x never interferes with the
        # neighbours I just read.
        cnt = {}
        ssum = {}
        ans = 0
        for x in nums:
            c = 1
            s = x
            for y in (x - 1, x + 1):
                if y in cnt:
                    c = (c + cnt[y]) % MOD
                    s = (s + ssum[y] + x * cnt[y]) % MOD
            cnt[x] = (cnt.get(x, 0) + c) % MOD
            ssum[x] = (ssum.get(x, 0) + s) % MOD
            ans = (ans + s) % MOD
        return ans
