# LeetCode 3134. Find the Median of the Uniqueness Array — Hard
# https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/
# Submission 2202025238 — Accepted, Python3
#
# My thinking: the median uniqueness is
# the smallest x such that at least half
# the subarrays have at most x distinct
# values. I count those subarrays for a
# given x with a sliding window — the
# window's right end only moves forward,
# so each count is linear — and
# binary-search the smallest x that
# reaches half.

from collections import defaultdict
from typing import List


class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2
        k = (total + 1) // 2

        def count_le(x: int) -> int:
            cnt = defaultdict(int)
            distinct = 0
            left = 0
            res = 0
            for right, v in enumerate(nums):
                if cnt[v] == 0:
                    distinct += 1
                cnt[v] += 1
                while distinct > x:
                    cnt[nums[left]] -= 1
                    if cnt[nums[left]] == 0:
                        distinct -= 1
                    left += 1
                res += right - left + 1
            return res

        lo, hi = 1, len(set(nums))
        while lo < hi:
            mid = (lo + hi) // 2
            if count_le(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
