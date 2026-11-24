# LeetCode 3444. Minimum Increments for Target Multiples in an Array — Hard
# https://leetcode.com/problems/minimum-increments-for-target-multiples-in-an-array/
# Submission 2202539318 — Accepted 590/590, Python3
import heapq
import math
from typing import List


class Solution:
    def minimumIncrements(self, nums: List[int], target: List[int]) -> int:
        # My thinking: each target must be covered by some element, and
        # one element can cover several targets at once if it is raised
        # to a multiple of their lcm. So I split the targets into groups,
        # one element per group, and the cheapest element for a group is
        # the cheapest way to reach a multiple of that group's lcm. For
        # each group only its 5 cheapest elements can matter (at most 3
        # other groups can take better ones), so I try every split and
        # every pick of distinct elements from those short lists.
        m = len(target)
        full = (1 << m) - 1
        # lcm of every nonempty subset of targets
        subset_lcm = {}
        for mask in range(1, 1 << m):
            l = 1
            for j in range(m):
                if mask >> j & 1:
                    l = l * target[j] // math.gcd(l, target[j])
            subset_lcm[mask] = l
        # 5 cheapest (cost, index) per subset
        best = {}
        for mask, l in subset_lcm.items():
            best[mask] = heapq.nsmallest(
                5, (((l - x % l) % l, i) for i, x in enumerate(nums)))
        # all set partitions of the target set, as lists of masks
        def partitions(rem):
            if rem == 0:
                yield []
                return
            low = rem & -rem
            sub = rem
            while sub:
                if sub & low:
                    for rest in partitions(rem ^ sub):
                        yield [sub] + rest
                sub = (sub - 1) & rem
        ans = math.inf
        for part in partitions(full):
            groups = [best[g] for g in part]
            # pick one distinct element per group, cheapest total
            def rec(gi, used, total):
                nonlocal ans
                if total >= ans:
                    return
                if gi == len(groups):
                    ans = total
                    return
                for cost, idx in groups[gi]:
                    if idx not in used:
                        used.add(idx)
                        rec(gi + 1, used, total + cost)
                        used.discard(idx)
            rec(0, set(), 0)
        return ans
