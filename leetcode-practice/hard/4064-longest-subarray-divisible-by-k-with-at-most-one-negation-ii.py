# LeetCode 4064. Longest Subarray Divisible by K with At Most One Negation II — Hard
# https://leetcode.com/problems/longest-subarray-divisible-by-k-with-at-most-one-negation-ii/
# Submission 2203589830 — Accepted, Python3
import numpy as np


class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        # My thinking: a subarray nums[l..r] has sum S, and
        # negating one element nums[t] inside it changes the
        # sum to S - 2*nums[t]. So it is valid when S is
        # already 0 mod k, or when some t inside it has
        # 2*nums[t] equal to S mod k. With prefix remainders
        # P, the sum of nums[l..r] is P[r+1] - P[l] mod k,
        # so for remainders a = P[l] and b = P[r+1] the
        # negation needs a t with 2*nums[t] equal to b - a
        # mod k, sitting between l and r. For fixed
        # remainders a and b, the longest such subarray uses
        # the earliest l with remainder a and the latest
        # r+1 with remainder b — any narrower choice is
        # shorter, and if no doubled residue lands inside
        # that widest window, none lands inside a narrower
        # one either. So I take the first and last
        # occurrence of every remainder, then for each
        # doubled residue d check all pairs (a, b = a+d)
        # at once with a vectorised searchsorted over the
        # sorted positions of d: the pair is good when the
        # first such position at or after first[a] still
        # lies before last[b]. The no-negation case is the
        # same idea with a = b. That is O(n + k^2) work.
        n = len(nums)
        pref = [0] * (n + 1)
        for i, x in enumerate(nums):
            pref[i + 1] = (pref[i] + x) % k
        first = [None] * k
        last = [None] * k
        for i, r in enumerate(pref):
            if first[r] is None:
                first[r] = i
            last[r] = i
        ans = 0
        for r in range(k):
            if first[r] is not None:
                ans = max(ans, last[r] - first[r])
        pos = [[] for _ in range(k)]
        for t, x in enumerate(nums):
            pos[(2 * x) % k].append(t)
        first_arr = np.array(
            [f if f is not None else n + 1 for f in first], dtype=np.int64
        )
        last_arr = np.array(
            [l if l is not None else -1 for l in last], dtype=np.int64
        )
        idx = np.arange(k, dtype=np.int64)
        for d in range(k):
            p = pos[d]
            if not p:
                continue
            p_arr = np.array(p, dtype=np.int64)
            L = last_arr[(idx + d) % k]
            j = np.searchsorted(p_arr, first_arr)
            inside = j < len(p_arr)
            hit = np.zeros(k, dtype=bool)
            hit[inside] = p_arr[j[inside]] < L[inside]
            cand = np.where(hit, L - first_arr, 0)
            m = int(cand.max())
            if m > ans:
                ans = m
        return ans
