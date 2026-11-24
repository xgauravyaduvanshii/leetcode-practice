# LeetCode 3533. Concatenated Divisibility — Hard
# https://leetcode.com/problems/concatenated-divisibility/
# Submission 2202812057 — Accepted, Python3
from typing import List
from functools import lru_cache


class Solution:
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        # My thinking: appending a number x with d digits multiplies
        # the running remainder by 10^d and adds x, all modulo k.
        # Whether the remaining numbers can finish the job depends
        # only on which numbers are left and the current remainder,
        # so I memoise that feasibility check over (subset, remainder)
        # and then build the answer greedily: at each position take
        # the smallest unused number that still leaves a feasible
        # completion. If none exists at all, the answer is empty.
        n = len(nums)
        dig = [len(str(v)) for v in nums]
        pow10 = [pow(10, d, k) for d in dig]

        @lru_cache(maxsize=None)
        def feasible(mask, r):
            if mask == 0:
                return r == 0
            m = mask
            i = 0
            while m:
                if m & 1:
                    if feasible(mask ^ (1 << i), (r * pow10[i] + nums[i]) % k):
                        return True
                m >>= 1
                i += 1
            return False

        if not feasible((1 << n) - 1, 0):
            return []
        res = []
        mask = (1 << n) - 1
        r = 0
        order = sorted(range(n), key=lambda i: (nums[i], i))
        for _ in range(n):
            for i in order:
                if not (mask >> i) & 1:
                    continue
                nr = (r * pow10[i] + nums[i]) % k
                if feasible(mask ^ (1 << i), nr):
                    res.append(nums[i])
                    mask ^= 1 << i
                    r = nr
                    break
        return res
