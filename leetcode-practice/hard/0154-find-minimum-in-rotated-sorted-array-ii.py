# LeetCode 154. Find Minimum in Rotated Sorted Array II — Hard
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
# Submission 2198390842 — Accepted, Python3
#
# My thinking: I binary search like the no-duplicates
# version, but equal ends are the tricky part — when
# the middle equals the right end I cannot tell which
# side the smallest value is on, so I just drop the
# right end by one and keep going. The search still
# shrinks every step, and whatever it lands on is
# the minimum.

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            elif nums[mid] < nums[hi]:
                hi = mid
            else:
                hi -= 1
        return nums[lo]
