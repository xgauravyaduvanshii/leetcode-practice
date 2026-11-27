# LeetCode 3261. Count Substrings That Satisfy K-Constraint II — Hard
# https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii/
# Submission 2202157436 — Accepted, Python3
#
# My thinking: a substring is valid when not
# both 0s and 1s exceed k. Sliding a window
# gives, for each right end r, the smallest
# left end that keeps it valid — left_bound[r].
# A query [l, r] counts, for every right end,
# the valid left ends: ends whose bound is at
# most l contribute r' - l + 1 each, the rest
# contribute r' - bound + 1. Prefix sums over
# left_bound plus a binary search split the
# two groups in O(log n) per query.

from typing import List


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        from bisect import bisect_right
        n = len(s)
        left_bound = [0] * n
        left = 0
        cnt0 = 0
        cnt1 = 0
        for r, ch in enumerate(s):
            if ch == '0':
                cnt0 += 1
            else:
                cnt1 += 1
            while cnt0 > k and cnt1 > k:
                if s[left] == '0':
                    cnt0 -= 1
                else:
                    cnt1 -= 1
                left += 1
            left_bound[r] = left
        pref = [0] * (n + 1)
        for i, v in enumerate(left_bound):
            pref[i + 1] = pref[i] + v
        ans = []
        for l, r in queries:
            length = r - l + 1
            sum_b1 = (l + r) * length // 2 + length
            pos = bisect_right(left_bound, l, l, r + 1)
            cnt_le = pos - l
            sum_le = pref[pos] - pref[l]
            sum_total = pref[r + 1] - pref[l]
            sum_max = cnt_le * l + (sum_total - sum_le)
            ans.append(sum_b1 - sum_max)
        return ans
