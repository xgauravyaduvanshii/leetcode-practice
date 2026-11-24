# LeetCode 3575. Maximum Good Subtree Score — Hard
# https://leetcode.com/problems/maximum-good-subtree-score/
# Submission 2202854803 — Accepted, Python3
from typing import List
from collections import defaultdict

MOD = 10 ** 9 + 7


class Solution:
    def goodSubtreeSum(self, vals: List[int], par: List[int]) -> int:
        # My thinking: a value whose own decimal digits repeat can
        # never be picked, so it gets mask -1. Otherwise each node
        # carries a digit mask, and a good subset is a choice of
        # nodes whose masks are pairwise disjoint. I do a tree DP
        # keyed by mask: merge the children's tables (only disjoint
        # masks combine), then optionally add this node itself, and
        # the node's best is the largest entry in its table. The
        # answer is the sum of every node's best, modulo 1e9+7.
        n = len(vals)
        children = defaultdict(list)
        for i in range(1, n):
            children[par[i]].append(i)

        def digit_mask(x):
            mask = 0
            for ch in str(x):
                d = ord(ch) - 48
                if mask & (1 << d):
                    return -1
                mask |= 1 << d
            return mask

        masks = [digit_mask(v) for v in vals]
        total = 0

        def dfs(u):
            nonlocal total
            dp = {0: 0}
            for v in children[u]:
                child = dfs(v)
                new = {}
                for m1, s1 in dp.items():
                    for m2, s2 in child.items():
                        if m1 & m2 == 0:
                            nm = m1 | m2
                            if s1 + s2 > new.get(nm, -1):
                                new[nm] = s1 + s2
                dp = new
            mu = masks[u]
            if mu != -1:
                extra = {}
                for m, s in dp.items():
                    if m & mu == 0:
                        nm = m | mu
                        if s + vals[u] > extra.get(nm, -1):
                            extra[nm] = s + vals[u]
                for nm, s in extra.items():
                    if s > dp.get(nm, -1):
                        dp[nm] = s
            total = (total + max(dp.values())) % MOD
            return dp

        dfs(0)
        return total
