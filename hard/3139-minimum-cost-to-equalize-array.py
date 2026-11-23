# LeetCode 3139. Minimum Cost to Equalize Array — Hard
# https://leetcode.com/problems/minimum-cost-to-equalize-array/
# Submission 2202031027 — Accepted, Python3
#
# My thinking: for a fixed target the
# cheapest mix of single and paired
# increments is forced by how much the
# smallest element must rise: its lifts
# can only pair with lifts of other
# elements, so any surplus lifts are
# singles. I evaluate that cost at the
# current maximum and around the target
# where the pairing first becomes tight,
# and keep the cheapest.

from typing import List


class Solution:
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        mx = max(nums)
        mn = min(nums)
        total = sum(nums)
        if n == 1:
            return 0
        if cost2 >= 2 * cost1:
            return (sum(mx - x for x in nums) * cost1) % MOD

        def cost(t: int) -> int:
            d = n * t - total
            mxd = t - mn
            excess = 2 * mxd - d
            if excess > 0:
                singles = excess
                pairs = d - mxd
            else:
                singles = d & 1
                pairs = (d - singles) // 2
            return pairs * cost2 + singles * cost1

        ans = cost(mx)
        if n > 2:
            num = total - 2 * mn
            if num > 0:
                t1 = (num + n - 3) // (n - 2)
            else:
                t1 = mx
            t1 = max(mx, t1)
            candidates = [t1, t1 + 1]
            if t1 > mx:
                candidates.append(t1 - 1)
            for t in candidates:
                ans = min(ans, cost(t))
        return ans % MOD
