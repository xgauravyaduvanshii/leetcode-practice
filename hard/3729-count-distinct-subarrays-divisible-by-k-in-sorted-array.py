# LeetCode 3729. Count Distinct Subarrays Divisible by K in Sorted Array — Hard
# https://leetcode.com/problems/count-distinct-subarrays-divisible-by-k-in-sorted-array/
# Submission 2203134433 — Accepted, Python3
from collections import Counter
from typing import List


class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:
        # My thinking: prefix sums modulo k count every good
        # subarray by position — two equal remainders bound a
        # subarray whose sum is divisible by k. That over-counts
        # only one kind of duplicate: in a sorted array, a value
        # sequence repeats only when it is all one value inside a
        # run of equal values, where a length-h block appears
        # m - h + 1 times positionally but is one distinct
        # sequence. So count all good subarrays, then walk each
        # maximal run and subtract m - h for every length h whose
        # block sum h * v is divisible by k.
        cnt = Counter({0: 1})
        ans = s = 0
        for x in nums:
            s = (s + x) % k
            ans += cnt[s]
            cnt[s] += 1
        n = len(nums)
        i = 0
        while i < n:
            j = i + 1
            while j < n and nums[j] == nums[i]:
                j += 1
            m = j - i
            for h in range(1, m + 1):
                if (h * nums[i]) % k == 0:
                    ans -= m - h
            i = j
        return ans
