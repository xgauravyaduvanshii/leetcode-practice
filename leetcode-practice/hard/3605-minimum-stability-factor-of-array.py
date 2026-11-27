# LeetCode 3605. Minimum Stability Factor of Array — Hard
# https://leetcode.com/problems/minimum-stability-factor-of-array/
# Submission 2202870138 — Accepted, Python3
import math
from typing import List


class Solution:
    def minStable(self, nums: List[int], maxC: int) -> int:
        # My thinking: a subarray is stable exactly when its GCD
        # is at least 2, so changing an element to 1 breaks every
        # window through it. For a target stability factor X, every
        # window of length X+1 must be broken, and the cheapest way
        # is greedy: scanning left to right, the first uncovered
        # stable window gets a 1 at its right end, which covers the
        # most future windows. That test is monotone in X, so I
        # binary search the smallest X I can afford. The window
        # GCDs come from the short list of distinct GCDs of
        # subarrays ending at each position.
        n = len(nums)

        def can(X):
            if X == 0:
                return sum(1 for x in nums if x >= 2) <= maxC
            if X >= n:
                return True
            count = 0
            last_break = -1
            gcds = []
            for r in range(n):
                new = [(nums[r], 1)]
                for g, cnt in gcds:
                    ng = math.gcd(g, nums[r])
                    if ng == new[-1][0]:
                        new[-1] = (ng, new[-1][1] + cnt)
                    else:
                        new.append((ng, cnt))
                gcds = new
                if r >= X:
                    l = r - X
                    if l <= last_break:
                        continue
                    offset = r - l
                    g = gcds[-1][0]
                    rem = offset
                    for gv, cnt in gcds:
                        if rem < cnt:
                            g = gv
                            break
                        rem -= cnt
                    if g >= 2:
                        count += 1
                        last_break = r
                        if count > maxC:
                            return False
            return count <= maxC

        lo, hi = 0, n
        best = n
        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                best = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return best
