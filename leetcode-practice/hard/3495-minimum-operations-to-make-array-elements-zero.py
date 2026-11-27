# LeetCode 3495. Minimum Operations to Make Array Elements Zero — Hard
# https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/
# Submission 2202713823 — Accepted, Python3

from bisect import bisect_right
from typing import List


class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        # My thinking: an element x needs t(x) touches, where t(x)
        # is how many times it must be divided by 4 to reach 0, so
        # t(x) = k exactly on [4^(k-1), 4^k - 1]. One operation
        # touches two elements, and the largest t(x) is only about
        # 15 while the total is huge, so the touches can always be
        # paired up with no operation wasting both touches on one
        # element. A query therefore costs ceil(total touches / 2),
        # and I get the total from a prefix sum over the powers
        # of 4.
        pow4 = [1]
        while pow4[-1] <= 10 ** 9:
            pow4.append(pow4[-1] * 4)
        pref = [0]
        s = 0
        for i in range(1, len(pow4)):
            s += i * (pow4[i] - pow4[i - 1])
            pref.append(s)

        def F(X):
            if X <= 0:
                return 0
            k = bisect_right(pow4, X)
            return pref[k - 1] + k * (X - pow4[k - 1] + 1)

        ans = 0
        for l, r in queries:
            total = F(r) - F(l - 1)
            ans += (total + 1) // 2
        return ans
