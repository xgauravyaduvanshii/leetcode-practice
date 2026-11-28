# LeetCode 2555. Maximize Win From Two Segments — Medium
# https://leetcode.com/problems/maximize-win-from-two-segments/
# Submission 2205064821 — Accepted, Python3
#
# My thinking: sort order is already given, so for each right end
# find the leftmost prize inside a length-k segment with bisect.
# pre[i] is the best single segment using only the first i prizes;
# pair it with a second segment ending at i and keep the best
# total. The two segments never need to overlap.
import bisect


class Solution:
    def maximizeWin(self, prizePositions: list[int], k: int) -> int:
        n = len(prizePositions)
        pre = [0] * (n + 1)
        for i, x in enumerate(prizePositions):
            j = bisect.bisect_left(prizePositions, x - k)
            pre[i + 1] = max(pre[i], i - j + 1)
        ans = 0
        for i, x in enumerate(prizePositions):
            j = bisect.bisect_left(prizePositions, x - k)
            ans = max(ans, pre[j] + (i - j + 1))
        return ans
