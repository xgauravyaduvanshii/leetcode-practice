# LeetCode 3509. Maximum Product of Subsequences With an Alternating Sum Equal to K — Hard
# https://leetcode.com/problems/maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k/
# Submission 2202762813 — Accepted, Python3
from typing import List


class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        # My thinking: I walk the array once, keeping for every
        # reachable (alternating sum, parity of length) the set of
        # products that stay within the limit. Reachability is tracked
        # on its own, apart from the products: a partial product that
        # already exceeds the limit is still a live subsequence, because
        # a later 0 multiplies it back to 0, which is within the limit.
        # Dropping over-limit states loses exactly those rescues, so I
        # keep the state reachable and only add a 0 product when a 0
        # arrives. Keeping the whole set of products (not just the max)
        # matters too, because a smaller product can survive a later
        # multiplication that pushes the largest one over the limit.
        reach = {(0, 0)}
        prod = {(0, 0): set()}
        for v in nums:
            items = list(reach)
            prod_snapshot = {key: set(val) for key, val in prod.items()}
            for (s, p) in items:
                ns = s + v if p == 0 else s - v
                np = 1 - p
                reach.add((ns, np))
                cur = prod.setdefault((ns, np), set())
                for p2 in prod_snapshot.get((s, p), set()):
                    nv = p2 * v
                    if nv <= limit:
                        cur.add(nv)
                if v == 0:
                    cur.add(0)
            reach.add((v, 1))
            if v <= limit:
                prod.setdefault((v, 1), set()).add(v)
        best = -1
        for p in (0, 1):
            for val in prod.get((k, p), set()):
                best = max(best, val)
        return best
