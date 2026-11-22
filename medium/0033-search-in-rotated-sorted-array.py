# LeetCode 33. Search in Rotated Sorted Array — Medium
# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Submission 2200871560 — Accepted, Python3
#
# My thinking: at every step one half of the array is
# still sorted, so I check which half that is and whether
# the target can live in it; if not, I throw that half
# away and keep searching the other one.

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
