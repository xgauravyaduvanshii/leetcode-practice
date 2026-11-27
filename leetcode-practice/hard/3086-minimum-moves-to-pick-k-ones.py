# LeetCode 3086. Minimum Moves to Pick K Ones — Hard
# https://leetcode.com/problems/minimum-moves-to-pick-k-ones/
# Submission 2201981752 — Accepted, Python3
#
# My thinking: I collect the positions of
# the ones. Gathering a run of consecutive
# ones is cheapest around their median,
# and prefix sums give that cost in
# constant time. Either I gather
# k - maxChanges existing ones and change
# the rest (two moves per change), or I
# gather just one, two or three ones and
# change the rest — a small gathered run
# can sit next to the changed ones. I try
# every window and keep the cheapest total.

from typing import List


class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        pos = [i for i, x in enumerate(nums) if x == 1]
        m = len(pos)
        pref = [0]
        for p in pos:
            pref.append(pref[-1] + p)

        def gather(l, r):
            if r - l <= 1:
                return 0
            mid = (l + r) // 2
            median = pos[mid]
            left = median * (mid - l) - (pref[mid] - pref[l])
            right = (pref[r] - pref[mid + 1]) - median * (r - mid - 1)
            return left + right

        L = k - maxChanges
        ans = float('inf')
        if L <= 0:
            ans = min(ans, 2 * k)
        if L > 0 and L <= m:
            best = float('inf')
            for i in range(m - L + 1):
                best = min(best, gather(i, i + L))
            ans = min(ans, best + 2 * maxChanges)
        for s in (1, 2, 3):
            if s < L or s > k or s > m:
                continue
            for i in range(m - s + 1):
                ans = min(ans, gather(i, i + s) + 2 * (k - s))
        return int(ans)
