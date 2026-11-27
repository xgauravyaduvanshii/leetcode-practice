# LeetCode 3957. Maximum Sum of M Non-Overlapping Subarrays II — Hard
# https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-ii/
# Submission 2203473024 — Accepted, Python3
from collections import deque
from typing import List


class Solution:
    def maximumSum(self, nums: List[int], m: int, l: int, r: int) -> int:
        # My thinking: let F(k) be the best sum using exactly k
        # subarrays. F is concave in k (each extra subarray can
        # only add less than the one before), so the Aliens trick
        # applies: charge a penalty lam per subarray and solve
        # the unconstrained problem — one linear DP where a
        # subarray ending at i is pref[i] plus the best of
        # dp[j] - pref[j] over j in [i-r, i-l], kept by a
        # monotone deque, with ties broken towards fewer
        # subarrays. If the best single subarray is negative,
        # every F(k) is negative and decreasing, so it is the
        # answer. Otherwise, if the penalty-free optimum already
        # uses at most m subarrays, it is the answer. If not, F
        # is still increasing on [1, m], so the answer is F(m):
        # binary-search the smallest lam whose optimum uses at
        # most m subarrays — at that lam, m is Lagrangian
        # optimal, so the value plus lam * m is exactly F(m).
        n = len(nums)
        pref = [0] * (n + 1)
        for i, x in enumerate(nums):
            pref[i + 1] = pref[i] + x

        def wqs(lam: int):
            dp = [0] * (n + 1)
            cnt = [0] * (n + 1)
            dq = deque()
            for i in range(1, n + 1):
                j = i - l
                if j >= 0:
                    val = dp[j] - pref[j]
                    while dq:
                        bj = dq[-1]
                        bv = dp[bj] - pref[bj]
                        if bv < val or (bv == val and cnt[bj] > cnt[j]):
                            dq.pop()
                        else:
                            break
                    dq.append(j)
                while dq and dq[0] < i - r:
                    dq.popleft()
                dp[i] = dp[i - 1]
                cnt[i] = cnt[i - 1]
                if dq:
                    bj = dq[0]
                    cand = pref[i] + (dp[bj] - pref[bj]) - lam
                    cc = cnt[bj] + 1
                    if cand > dp[i] or (cand == dp[i] and cc < cnt[i]):
                        dp[i] = cand
                        cnt[i] = cc
            return dp[n], cnt[n]

        def best_one() -> int:
            NEG = -10 ** 18
            dp_prev = [0] * (n + 1)
            dp_cur = [NEG] * (n + 1)
            dq = deque()
            for i in range(1, n + 1):
                j = i - l
                if j >= 0:
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
            return dp_cur[n]

        best1 = best_one()
        if best1 < 0:
            return best1
        val0, c0 = wqs(0)
        if c0 <= m:
            return val0
        lo, hi = -10 ** 11, 10 ** 11
        while lo < hi:
            mid = (lo + hi) // 2
            _, c = wqs(mid)
            if c <= m:
                hi = mid
            else:
                lo = mid + 1
        lam = lo
        val, _ = wqs(lam)
        return val + lam * m
