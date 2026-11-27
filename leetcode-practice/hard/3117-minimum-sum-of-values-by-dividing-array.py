# LeetCode 3117. Minimum Sum of Values by Dividing Array — Hard
# https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/
# Submission 2202008803 — Accepted, Python3
#
# My thinking: I scan the array keeping
# a small map from (segments finished,
# running AND of the current segment) to
# the cheapest cost so far. The AND only
# ever loses bits, so few states survive.
# When a segment's AND reaches its
# target I may close it, adding the
# segment's last element to the cost;
# the answer is the cheapest cost with
# all segments closed.

from typing import List


class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        m = len(andValues)
        dp = {0: 0}
        for x in nums:
            ndp = {}
            for key, cost in dp.items():
                j = key >> 18
                cur = (key & 262143) - 1
                if cur == -1:
                    if j >= m:
                        continue
                    target = andValues[j]
                    if (x & target) != target:
                        continue
                    k2 = (j << 18) | (x + 1)
                    if k2 not in ndp or cost < ndp[k2]:
                        ndp[k2] = cost
                    if x == target:
                        k3 = (j + 1) << 18
                        nc = cost + x
                        if k3 not in ndp or nc < ndp[k3]:
                            ndp[k3] = nc
                else:
                    target = andValues[j]
                    nc_and = cur & x
                    if (nc_and & target) != target:
                        continue
                    k2 = (j << 18) | (nc_and + 1)
                    if k2 not in ndp or cost < ndp[k2]:
                        ndp[k2] = cost
                    if nc_and == target:
                        k3 = (j + 1) << 18
                        nc = cost + x
                        if k3 not in ndp or nc < ndp[k3]:
                            ndp[k3] = nc
            dp = ndp
            if not dp:
                break
        return dp.get(m << 18, -1)
