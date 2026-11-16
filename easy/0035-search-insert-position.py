# LeetCode 35. Search Insert Position — Easy
# https://leetcode.com/problems/search-insert-position/
# Submission 2197280702 — Accepted, Python3
#
# My thinking: the array is sorted, so binary search is
# the natural fit. I keep narrowing the range until I
# either find the target, or the left pointer lands
# exactly where the target should be inserted.

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left
