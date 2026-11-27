# LeetCode 3187. Peaks in Array — Hard
# https://leetcode.com/problems/peaks-in-array/
# Submission 2202069709 — Accepted, Python3
#
# My thinking: a peak can only change at
# the updated index and its two
# neighbours, so I keep all peaks in a
# Fenwick tree: point updates on at most
# three positions, and a range query
# counts the peaks strictly inside
# [l, r]. A range shorter than two holds
# no peak.

from typing import List


class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        bit = [0] * (n + 2)

        def bit_add(i, delta):
            i += 1
            while i <= n + 1:
                bit[i] += delta
                i += i & -i

        def bit_sum(i):
            if i < 0:
                return 0
            i += 1
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        def is_peak(i):
            return 1 if 0 < i < n - 1 and nums[i] > nums[i - 1] and nums[i] > nums[i + 1] else 0

        peak = [0] * n
        for i in range(n):
            peak[i] = is_peak(i)
            if peak[i]:
                bit_add(i, 1)
        ans = []
        for q in queries:
            if q[0] == 1:
                l, r = q[1], q[2]
                if r - l < 2:
                    ans.append(0)
                else:
                    ans.append(bit_sum(r - 1) - bit_sum(l))
            else:
                idx, val = q[1], q[2]
                nums[idx] = val
                for i in (idx - 1, idx, idx + 1):
                    if 0 < i < n - 1:
                        nv = is_peak(i)
                        if nv != peak[i]:
                            bit_add(i, nv - peak[i])
                            peak[i] = nv
        return ans
