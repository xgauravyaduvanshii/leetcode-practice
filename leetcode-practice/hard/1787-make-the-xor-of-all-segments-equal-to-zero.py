# LeetCode 1787. Make the XOR of All Segments Equal to Zero — Hard
# https://leetcode.com/problems/make-the-xor-of-all-segments-equal-to-zero/
# Submission 2201163280 — Accepted, Python3
#
# My thinking: positions that are k apart must all
# end up equal, so I group them and, group by
# group, keep the cheapest cost for every xor so
# far — keeping the group's most common value is
# cheapest, changing the whole group costs the
# group size no matter what value I pick.

from collections import Counter

class Solution:
    def minChanges(self, nums: list[int], k: int) -> int:
        groups = [Counter() for _ in range(k)]
        for i, v in enumerate(nums):
            groups[i % k][v] += 1
        INF = 10 ** 9
        dp = [INF] * 1024
        dp[0] = 0
        for i in range(k):
            cnt = groups[i]
            size = sum(cnt.values())
            best = min(dp)
            ndp = [best + size] * 1024
            for x in range(1024):
                if dp[x] == INF:
                    continue
                for v, f in cnt.items():
                    nx = x ^ v
                    ndp[nx] = min(ndp[nx], dp[x] + size - f)
            dp = ndp
        return dp[0]
