# LeetCode 3538. Merge Operations for Minimum Travel Time — Hard
# https://leetcode.com/problems/merge-operations-for-minimum-travel-time/
# Submission 2202816256 — Accepted, Python3
from typing import List


class Solution:
    def minTravelTime(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:
        # My thinking: merging joins neighbouring signs into groups,
        # and a group's time is the sum of its signs' times while its
        # representative is its rightmost sign. The road then costs,
        # for each group except the last, the distance to the next
        # group's representative times that group's time sum. A
        # group's cost is only known once the next representative is
        # chosen, so my DP state keeps the last two representatives:
        # dp[prev][i][g] is the cheapest cost for groups ending at i,
        # counting every segment except the one starting at i, and
        # extending to a new representative j adds the segment
        # [position[i], position[j]] at the group ending at i.
        INF = float("inf")
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + time[i]
        groups_needed = n - k
        dp = [[[INF] * (groups_needed + 1) for _ in range(n)] for _ in range(n + 1)]
        dp[0][0][1] = 0
        for i in range(n):
            for prev_idx in range(n + 1):
                prev = prev_idx - 1
                if prev >= i:
                    continue
                for g in range(1, groups_needed + 1):
                    cur = dp[prev_idx][i][g]
                    if cur == INF:
                        continue
                    S = pref[i + 1] - pref[prev + 1]
                    for j in range(i + 1, n):
                        if g + 1 > groups_needed:
                            break
                        nv = cur + (position[j] - position[i]) * S
                        if nv < dp[i + 1][j][g + 1]:
                            dp[i + 1][j][g + 1] = nv
        ans = INF
        for prev_idx in range(n + 1):
            ans = min(ans, dp[prev_idx][n - 1][groups_needed])
        return ans
