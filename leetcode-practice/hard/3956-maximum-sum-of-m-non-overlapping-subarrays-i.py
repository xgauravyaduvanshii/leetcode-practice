# LeetCode 3956. Maximum Sum of M Non-Overlapping Subarrays I — Hard
# https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-i/
# Submission 2203454215 — Accepted, Python3
from collections import deque
from typing import List


class Solution:
    def maximumSum(self, nums: List[int], m: int, l: int, r: int) -> int:
        # My thinking: dp[k][i] is the best sum using exactly k
        # subarrays inside the first i elements. Either the ith
        # element is unused (carry dp[k][i-1] forward) or a
        # subarray ends at i: its start j ranges over
        # [i-r, i-l], giving dp[k-1][j] + pref[i] - pref[j].
        # That is pref[i] plus the best of dp[k-1][j] - pref[j]
        # over a sliding window, which a monotone deque keeps in
        # O(1) amortised time — so each k costs one linear pass.
        # The answer is the best over k = 1..m, since at least
        # one subarray must be taken and extra ones may be
        # skipped when they would only lower the sum.
        n = len(nums)
        pref = [0] * (n + 1)
        for i, x in enumerate(nums):
            pref[i + 1] = pref[i] + x
        NEG = -10 ** 18
        dp_prev = [0] * (n + 1)
        ans = NEG
        for k in range(1, m + 1):
            dp_cur = [NEG] * (n + 1)
            dq = deque()
            for i in range(1, n + 1):
                j = i - l
                if j >= 0 and dp_prev[j] > NEG // 2:
                    val = dp_prev[j] - pref[j]
                    while dq and dp_prev[dq[-1]] - pref[dq[-1]] <= val:
                        dq.pop()
                    dq.append(j)
                while dq and dq[0] < i - r:
                    dq.popleft()
                if dq:
                    dp_cur[i] = pref[i] + (dp_prev[dq[0]] - pref[dq[0]])
                if dp_cur[i - 1] > dp_cur[i]:
                    dp_cur[i] = dp_cur[i - 1]
            if dp_cur[n] > ans:
                ans = dp_cur[n]
            dp_prev = dp_cur
        return ans
