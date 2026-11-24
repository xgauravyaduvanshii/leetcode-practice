# LeetCode 3420. Count Non-Decreasing Subarrays After K Operations — Hard
# https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/
# Submission 2202519950 — Accepted 731/731, Python3
from collections import deque
from typing import List


class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        # My thinking: to fix a subarray I raise each element to
        # the running maximum, so its cost is the sum of the gaps
        # below that maximum. I slide a window and keep its cost
        # in `s`: a monotonic deque holds the record maxima, so
        # appending a value only adds (window max - value). When
        # the cost passes k I drop the left end — its record ruled
        # the stretch up to its next greater element, and I walk
        # that stretch's own records to subtract exactly what
        # they stop costing. Every index enters and leaves the
        # deque once, so the whole pass is linear.
        n = len(nums)
        ng = [n] * n
        q = deque()
        s = 0
        ans = 0
        j = 0
        for i in range(n):
            while q and nums[q[-1]] < nums[i]:
                ng[q.pop()] = i
            q.append(i)
            s += nums[q[0]] - nums[i]
            while s > k:
                old = nums[j]
                lim = min(i + 1, ng[j])
                j += 1
                if q and q[0] < j:
                    q.popleft()
                c = j
                while c < lim:
                    nxt = min(lim, ng[c])
                    s -= (old - nums[c]) * (nxt - c)
                    c = nxt
            ans += i - j + 1
        return ans
