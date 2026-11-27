# LeetCode 3995. Minimum Cost to Convert String III — Hard
# https://leetcode.com/problems/minimum-cost-to-convert-string-iii/
# Submission 2203501190 — Accepted, Python3
from typing import List


class Solution:
    def minCost(self, source: str, target: str, rules: List[List[str]], costs: List[int]) -> int:
        # My thinking: each position is used by at most
        # one rule application, so the string under a rule
        # is still the original source there — a rule can
        # only help if its pattern matches the source
        # segment and its replacement equals the target
        # segment. That turns the problem into a shortest
        # path over positions: dp[i] is the cheapest cost
        # of converting the first i characters. From i we
        # may leave a matching character untouched for
        # free, or apply any rule whose replacement equals
        # target[i:i+L] and whose pattern matches
        # source[i:i+L], paying its base cost plus one per
        # wildcard. Grouping the rules by (length,
        # replacement) means only the few rules that can
        # produce the needed target segment are tried.
        n = len(source)
        INF = float("inf")
        by = {}
        for (pat, rep), c in zip(rules, costs):
            by.setdefault((len(pat), rep), []).append((pat, c + pat.count("*")))
        lengths = sorted({L for (L, _) in by})
        dp = [INF] * (n + 1)
        dp[0] = 0
        for i in range(n):
            if dp[i] == INF:
                continue
            if source[i] == target[i] and dp[i] < dp[i + 1]:
                dp[i + 1] = dp[i]
            for L in lengths:
                if i + L > n:
                    continue
                seg_t = target[i:i + L]
                for pat, c in by.get((L, seg_t), ()):
                    seg_s = source[i:i + L]
                    ok = True
                    for pc, sc in zip(pat, seg_s):
                        if pc != "*" and pc != sc:
                            ok = False
                            break
                    if ok and dp[i] + c < dp[i + L]:
                        dp[i + L] = dp[i] + c
        return dp[n] if dp[n] != INF else -1
