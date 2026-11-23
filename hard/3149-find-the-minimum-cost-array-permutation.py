# LeetCode 3149. Find the Minimum Cost Array Permutation — Hard
# https://leetcode.com/problems/find-the-minimum-cost-array-permutation/
# Submission 2202040337 — Accepted, Python3
#
# My thinking: the cost of a permutation
# is a tour starting at 0, so I run a
# Held-Karp DP over subsets: f[mask][last]
# is the cheapest cost of visiting exactly
# the set mask and ending at last, keeping
# the lexicographically smallest path on
# ties. The answer closes the tour back
# to 0.

from typing import List


class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        N = 1 << n
        INF = 10 ** 9
        cost = [[abs(a - nums[b]) for b in range(n)] for a in range(n)]
        f = [[INF] * n for _ in range(N)]
        path = [[None] * n for _ in range(N)]
        f[1][0] = 0
        path[1][0] = (0,)
        for mask in range(N):
            if not (mask & 1):
                continue
            fmask = f[mask]
            pmask = path[mask]
            for last in range(n):
                cur = fmask[last]
                if cur == INF:
                    continue
                p = pmask[last]
                crow = cost[last]
                rem = (~mask) & (N - 1)
                while rem:
                    lsb = rem & -rem
                    nxt = lsb.bit_length() - 1
                    rem ^= lsb
                    nmask = mask | lsb
                    val = cur + crow[nxt]
                    fv = f[nmask][nxt]
                    if val < fv:
                        f[nmask][nxt] = val
                        path[nmask][nxt] = p + (nxt,)
                    elif val == fv:
                        np = p + (nxt,)
                        if np < path[nmask][nxt]:
                            path[nmask][nxt] = np
        full = N - 1
        best_cost = INF
        best_path = None
        for last in range(n):
            pth = path[full][last]
            if pth is None:
                continue
            total = f[full][last] + cost[last][0]
            if best_path is None or total < best_cost or (total == best_cost and pth < best_path):
                best_cost = total
                best_path = pth
        return list(best_path)
