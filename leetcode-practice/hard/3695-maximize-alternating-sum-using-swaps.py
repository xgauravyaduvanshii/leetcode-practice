# LeetCode 3695. Maximize Alternating Sum Using Swaps — Hard
# https://leetcode.com/problems/maximize-alternating-sum-using-swaps/
# Submission 2203045071 — Accepted, Python3
from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        # My thinking: swaps link indices into connected components,
        # and inside one component the values can be rearranged
        # freely, since any permutation is reachable by swaps. An
        # even index adds its value to the sum and an odd index
        # subtracts it, so in each component I put the biggest
        # values on the even spots and the smallest on the odd ones.
        n = len(nums)
        parent = list(range(n))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for p, q in swaps:
            rp, rq = find(p), find(q)
            if rp != rq:
                parent[rp] = rq

        groups = {}
        for i in range(n):
            groups.setdefault(find(i), []).append(i)

        ans = 0
        for idxs in groups.values():
            vals = sorted((nums[i] for i in idxs), reverse=True)
            evens = sum(1 for i in idxs if i % 2 == 0)
            ans += sum(vals[:evens]) - sum(vals[evens:])
        return ans
