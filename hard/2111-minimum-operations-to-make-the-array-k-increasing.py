# LeetCode 2111. Minimum Operations to Make the Array K-Increasing — Hard
# https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/
# Submission 2201576639 — Accepted, Python3
#
# My thinking: one operation rewrites a single
# element to anything, so the elements I leave
# alone have to already rise along their chain
# — each of the k chains keeps its longest
# non-decreasing run, and everything else is
# one operation each.

import bisect


class Solution:
    def kIncreasing(self, arr: list[int], k: int) -> int:
        ops = 0
        for start in range(k):
            chain = arr[start::k]
            tails = []
            for x in chain:
                i = bisect.bisect_right(tails, x)
                if i == len(tails):
                    tails.append(x)
                else:
                    tails[i] = x
            ops += len(chain) - len(tails)
        return ops
