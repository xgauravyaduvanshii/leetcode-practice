# LeetCode 3939. Count Non Adjacent Subsets in a Rooted Tree — Hard
# https://leetcode.com/problems/count-non-adjacent-subsets-in-a-rooted-tree/
# Submission 2203432171 — Accepted, Python3
from typing import List


class Solution:
    def countValidSubsets(self, parent: List[int], nums: List[int], k: int) -> int:
        # My thinking: a tree DP with two states per node.
        # dp0[u] counts the ways in u's subtree with sums
        # by residue mod k when u is not selected, dp1[u]
        # the same when u is selected. A child contributes
        # dp0 + dp1 to a non-selected parent (the child
        # may be either) but only dp0 to a selected parent
        # (no two adjacent nodes may both be selected).
        # Merging a child is a knapsack convolution over
        # residues: new[(a + b) % k] += dp[a] * child[b].
        # Only residues with a nonzero count are stored,
        # which keeps the merges small. Since parent[i] <
        # i, processing nodes in reverse index order
        # finalises every child before its parent. The
        # answer is the residue-0 count at the root over
        # both states, minus 1 for the empty subset.
        MOD = 10 ** 9 + 7
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)
        dp0 = [None] * n
        dp1 = [None] * n
        for u in range(n - 1, -1, -1):
            cur0 = {0: 1}
            cur1 = {nums[u] % k: 1}
            for ch in children[u]:
                tot = dict(dp0[ch])
                for r, v in dp1[ch].items():
                    tot[r] = (tot.get(r, 0) + v) % MOD
                nxt0 = {}
                for a, va in cur0.items():
                    for b, vb in tot.items():
                        nxt0[(a + b) % k] = (nxt0.get((a + b) % k, 0) + va * vb) % MOD
                cur0 = nxt0
                nxt1 = {}
                for a, va in cur1.items():
                    for b, vb in dp0[ch].items():
                        nxt1[(a + b) % k] = (nxt1.get((a + b) % k, 0) + va * vb) % MOD
                cur1 = nxt1
            dp0[u] = cur0
            dp1[u] = cur1
        return (dp0[0].get(0, 0) + dp1[0].get(0, 0) - 1) % MOD
