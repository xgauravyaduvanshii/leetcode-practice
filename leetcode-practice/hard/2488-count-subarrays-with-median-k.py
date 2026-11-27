# LeetCode 2488. Count Subarrays With Median K — Hard
# https://leetcode.com/problems/count-subarrays-with-median-k/
# Submission 2201776549 — Accepted, Python3
#
# My thinking: I turn every number into
# +1 if it beats k, -1 if it loses to k,
# and 0 for k itself — a subarray holding
# k has median k exactly when its balance
# is 0 or 1, so I count how many left
# borders give each balance and sweep the
# right border past k.

from collections import Counter


class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        pos = nums.index(k)
        pref = [0] * (n + 1)
        for i, x in enumerate(nums):
            if x > k:
                pref[i + 1] = pref[i] + 1
            elif x < k:
                pref[i + 1] = pref[i] - 1
            else:
                pref[i + 1] = pref[i]
        left = Counter(pref[:pos + 1])
        ans = 0
        for r in range(pos, n):
            bal = pref[r + 1]
            ans += left[bal] + left[bal - 1]
        return ans
