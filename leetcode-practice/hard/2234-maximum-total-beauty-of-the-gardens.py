# LeetCode 2234. Maximum Total Beauty of the Gardens — Hard
# https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/
# Submission 2201629870 — Accepted, Python3
#
# My thinking: I sort the gardens, finish
# the biggest ones first, and spend what's
# left raising the smallest of the rest —
# for each count of finished gardens I
# binary-search the highest floor the rest
# can reach.

import bisect


class Solution:
    def maximumBeauty(self, flowers: list[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        flowers.sort()
        n = len(flowers)
        pref = [0]
        for f in flowers:
            pref.append(pref[-1] + f)
        need = [0] * (n + 1)
        for i in range(1, n + 1):
            need[i] = need[i - 1] + max(0, target - flowers[n - i])
        ans = 0
        for i in range(n + 1):
            if need[i] > newFlowers:
                break
            rem = newFlowers - need[i]
            if i == n:
                ans = max(ans, n * full)
                continue
            m = n - i
            incomplete = bisect.bisect_left(flowers, target, 0, m)
            if incomplete == 0:
                # Every remaining garden is already complete.
                ans = max(ans, n * full)
                continue
            lo, hi = 0, target - 1
            best = 0
            while lo <= hi:
                mid = (lo + hi) // 2
                cnt = bisect.bisect_left(flowers, mid, 0, m)
                cost = cnt * mid - pref[cnt]
                if cost <= rem:
                    best = mid
                    lo = mid + 1
                else:
                    hi = mid - 1
            ans = max(ans, i * full + best * partial)
        return ans
