# LeetCode 2602. Minimum Operations to Make All Array Elements Equal — Medium
# https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/
# Submission 2205098825 — Accepted, Python3
#
# My thinking: sort once with prefix sums. For a query q, the
# elements below q each cost q - x and the ones at or above
# each cost x - q; bisect finds the split, and both sides come
# straight from the prefix sums.
import bisect


class Solution:
    def minOperations(self, nums: list[int], queries: list[int]) -> list[int]:
        nums.sort()
        n = len(nums)
        pref = [0]
        for x in nums:
            pref.append(pref[-1] + x)
        ans = []
        for q in queries:
            i = bisect.bisect_left(nums, q)
            left = q * i - pref[i]
            right = (pref[n] - pref[i]) - q * (n - i)
            ans.append(left + right)
        return ans
