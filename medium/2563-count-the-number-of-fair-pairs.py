# LeetCode 2563. Count the Number of Fair Pairs — Medium
# https://leetcode.com/problems/count-the-number-of-fair-pairs/
# Submission 2205069585 — Accepted, Python3
#
# My thinking: sort, then for each left element the valid partners
# form one contiguous block — bisect gives its ends in the sorted
# array, and only partners after i are counted.
import bisect


class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        for i, x in enumerate(nums):
            lo = bisect.bisect_left(nums, lower - x, i + 1)
            hi = bisect.bisect_right(nums, upper - x, i + 1)
            ans += hi - lo
        return ans
