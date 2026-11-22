# LeetCode 1923. Longest Common Subpath — Hard
# https://leetcode.com/problems/longest-common-subpath/
# Submission 2201234565 — Accepted, Python3
#
# My thinking: I binary search the length and
# check it with a rolling hash — for each path I
# collect the hashes of all its windows of that
# length, and the length works when some hash
# survives in every path.

class Solution:
    def longestCommonSubpath(self, n: int, paths: list[list[int]]) -> int:
        MOD1, MOD2 = 10 ** 9 + 7, 10 ** 9 + 9
        BASE = 100007

        def feasible(L):
            if L == 0:
                return True
            common = None
            for path in paths:
                if len(path) < L:
                    return False
                h1 = h2 = 0
                p1 = p2 = 1
                for i in range(L):
                    h1 = (h1 * BASE + path[i] + 1) % MOD1
                    h2 = (h2 * BASE + path[i] + 1) % MOD2
                    if i < L - 1:
                        p1 = p1 * BASE % MOD1
                        p2 = p2 * BASE % MOD2
                s = {(h1, h2)}
                for i in range(L, len(path)):
                    h1 = ((h1 - (path[i - L] + 1) * p1) * BASE + path[i] + 1) % MOD1
                    h2 = ((h2 - (path[i - L] + 1) * p2) * BASE + path[i] + 1) % MOD2
                    s.add((h1, h2))
                common = s if common is None else (common & s)
                if not common:
                    return False
            return bool(common)

        lo, hi = 0, min(len(p) for p in paths)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if feasible(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
