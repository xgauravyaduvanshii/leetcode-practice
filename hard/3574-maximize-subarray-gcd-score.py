# LeetCode 3574. Maximize Subarray GCD Score — Hard
# https://leetcode.com/problems/maximize-subarray-gcd-score/
# Submission 2202852583 — Accepted, Python3
import math
from typing import List


class Solution:
    def maxGCDScore(self, nums: List[int], k: int) -> int:
        # My thinking: doubling an element can only raise a
        # subarray's GCD to at most twice its old value, and only
        # when every element holding the smallest power of two gets
        # doubled — the odd part of the GCD never changes. So for
        # each subarray I keep its GCD, the smallest 2-adic
        # valuation inside it, and how many elements sit at that
        # minimum; the score is length times GCD, doubled when that
        # count fits in the budget.
        n = len(nums)
        v2 = []
        for x in nums:
            c = 0
            while x % 2 == 0:
                x //= 2
                c += 1
            v2.append(c)
        best = 0
        for l in range(n):
            g = 0
            m = 10 ** 9
            cnt = 0
            for r in range(l, n):
                g = math.gcd(g, nums[r])
                if v2[r] < m:
                    m = v2[r]
                    cnt = 1
                elif v2[r] == m:
                    cnt += 1
                score = (r - l + 1) * g * (2 if cnt <= k else 1)
                if score > best:
                    best = score
        return best
