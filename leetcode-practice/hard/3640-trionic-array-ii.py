# LeetCode 3640. Trionic Array II — Hard
# https://leetcode.com/problems/trionic-array-ii/
# Submission 2202926179 — Accepted, Python3
from collections import deque
from typing import List


class Solution:
    def maxTrionicSum(self, nums: List[int]) -> int:
        # My thinking: a trionic subarray is an increasing run up
        # to a peak p, a decreasing run down to a valley q, then an
        # increasing run again. For the outer runs I take the best
        # suffix/prefix of the run: because the run is strictly
        # increasing, extending it only helps while the new element
        # is positive, so the best increasing subarray ending at p
        # (or starting at q) is the run trimmed at the first
        # non-positive element. For the middle run, fixing q, the
        # value of a peak p is L[p] plus the stretch p+1..q, which
        # is L[p] - prefix[p+1] plus a term that only depends on q,
        # so I sweep q left to right keeping the best peak of the
        # current decreasing run in a sliding-window deque.
        n = len(nums)
        prefix = [0] * (n + 1)
        for i, v in enumerate(nums):
            prefix[i + 1] = prefix[i] + v

        # best1[i]: best sum of an increasing subarray ending at i
        # (length >= 1). L[i]: same with length >= 2, else None.
        best1 = [0] * n
        L = [None] * n
        for i in range(n):
            if i > 0 and nums[i - 1] < nums[i]:
                best1[i] = nums[i] + max(0, best1[i - 1])
                L[i] = nums[i] + best1[i - 1]
            else:
                best1[i] = nums[i]

        # best1r[i]: best sum of an increasing subarray starting
        # at i (length >= 1). R[i]: same with length >= 2.
        best1r = [0] * n
        R = [None] * n
        for i in range(n - 1, -1, -1):
            if i + 1 < n and nums[i] < nums[i + 1]:
                best1r[i] = nums[i] + max(0, best1r[i + 1])
                R[i] = nums[i] + best1r[i + 1]
            else:
                best1r[i] = nums[i]

        ans = None
        # Deque of (p, L[p] - prefix[p+1]) with decreasing values,
        # p ranging over the current decreasing run ending at q.
        dq = deque()
        run_start = 0
        for q in range(n):
            if q > 0 and nums[q - 1] > nums[q]:
                pass  # run continues, run_start unchanged
            else:
                run_start = q
            p = q - 1
            if p >= 0 and L[p] is not None:
                val = L[p] - prefix[p + 1]
                while dq and dq[-1][1] <= val:
                    dq.pop()
                dq.append((p, val))
            while dq and dq[0][0] < run_start:
                dq.popleft()
            if dq and R[q] is not None:
                total = dq[0][1] + prefix[q + 1] + R[q] - nums[q]
                ans = total if ans is None else max(ans, total)
        return ans
