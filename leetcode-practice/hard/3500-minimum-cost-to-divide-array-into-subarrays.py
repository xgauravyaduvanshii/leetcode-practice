# LeetCode 3500. Minimum Cost to Divide Array Into Subarrays — Hard
# https://leetcode.com/problems/minimum-cost-to-divide-array-into-subarrays/
# Submission 2202718370 — Accepted, Python3

from collections import deque
from typing import List


class Solution:
    def minimumCost(self, nums: List[int], cost: List[int], k: int) -> int:
        # My thinking: let P and C be the prefix sums of nums and
        # cost. Splitting the first j elements into i subarrays
        # costs dp[i-1][m] + (P[j] + k*i) * (C[j] - C[m]) for the
        # last cut after m. Expanding, the m-part is a line in P[j]
        # with slope -C[m] and intercept dp[i-1][m] - k*i*C[m].
        # Costs are positive, so C[m] grows and the slopes arrive
        # in decreasing order while the queries P[j] grow, which
        # is exactly the monotone convex hull trick with a deque:
        # lines are added at the back and the best line is popped
        # from the front. All comparisons use integers, no floats.
        n = len(nums)
        P = [0] * (n + 1)
        C = [0] * (n + 1)
        for i in range(n):
            P[i + 1] = P[i] + nums[i]
            C[i + 1] = C[i] + cost[i]
        INF = float("inf")
        dp_prev = [INF] * (n + 1)
        dp_prev[0] = 0
        ans = INF
        for i in range(1, n + 1):
            dq = deque()

            def bad(l1, l2, l3):
                m1, b1 = l1
                m2, b2 = l2
                m3, b3 = l3
                return (b2 - b1) * (m2 - m3) >= (b3 - b2) * (m1 - m2)

            def ev(line, x):
                return line[0] * x + line[1]

            dp_cur = [INF] * (n + 1)
            for j in range(1, n + 1):
                m = j - 1
                if m >= i - 1 and dp_prev[m] < INF:
                    nl = (-C[m], dp_prev[m] - k * i * C[m])
                    while len(dq) >= 2 and bad(dq[-2], dq[-1], nl):
                        dq.pop()
                    dq.append(nl)
                if dq:
                    x = P[j]
                    while len(dq) >= 2 and ev(dq[0], x) >= ev(dq[1], x):
                        dq.popleft()
                    dp_cur[j] = (P[j] + k * i) * C[j] + ev(dq[0], x)
            dp_prev = dp_cur
            ans = min(ans, dp_prev[n])
        return ans
