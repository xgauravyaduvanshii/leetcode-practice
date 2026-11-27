# LeetCode 3985. Palindromic Subarray Sum — Hard
# https://leetcode.com/problems/palindromic-subarray-sum/
# Submission 2203497335 — Accepted, Python3
from typing import List


class Solution:
    def getSum(self, nums: List[int]) -> int:
        # My thinking: every number is positive, so for a
        # fixed centre a longer palindrome always has a
        # larger sum — the best palindrome at that centre
        # is the longest one. Manacher's algorithm finds
        # the longest odd and even palindrome at every
        # centre in linear time, and prefix sums give each
        # one's sum in O(1). A single element is always a
        # palindrome, so the answer is at least max(nums).
        # The sum can reach 10^5 * 10^9, so it needs 64
        # bits in C++, but Python ints hold it directly.
        n = len(nums)
        pref = [0] * (n + 1)
        for i, x in enumerate(nums):
            pref[i + 1] = pref[i] + x
        d1 = [0] * n
        l, r = 0, -1
        for i in range(n):
            k = 1 if i > r else min(d1[l + r - i], r - i + 1)
            while i - k >= 0 and i + k < n and nums[i - k] == nums[i + k]:
                k += 1
            d1[i] = k
            if i + k - 1 > r:
                l, r = i - k + 1, i + k - 1
        d2 = [0] * n
        l, r = 0, -1
        for i in range(n):
            k = 0 if i > r else min(d2[l + r - i + 1], r - i + 1)
            while i - k - 1 >= 0 and i + k < n and nums[i - k - 1] == nums[i + k]:
                k += 1
            d2[i] = k
            if i + k - 1 > r:
                l, r = i - k, i + k - 1
        ans = max(nums)
        for i in range(n):
            if d1[i] > 0:
                ans = max(ans, pref[i + d1[i]] - pref[i - d1[i] + 1])
            if d2[i] > 0:
                ans = max(ans, pref[i + d2[i]] - pref[i - d2[i]])
        return ans
