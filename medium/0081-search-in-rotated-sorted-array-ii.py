# LeetCode 81. Search in Rotated Sorted Array II — Medium
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
# Submission 2203957858 — Accepted, Python3
#
# My thinking:
# The array is sorted but rotated, and it may contain duplicates.
# A plain binary search still works most of the time: compare nums[mid]
# with nums[left] to tell which half is sorted, then check whether the
# target lies inside that sorted half and shrink the window accordingly.
# The only trouble is duplicates: when nums[left] == nums[mid] == nums[right],
# we cannot tell which half is sorted, so we shrink both ends by one and
# try again. In the worst case (all duplicates) that is linear, but it is
# correct and fast on typical inputs.

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True

            # Duplicates hide which half is sorted: shrink both ends.
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            # Left half is sorted.
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right half is sorted.
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False


if __name__ == "__main__":
    s = Solution()
    # Sample 1: target present.
    assert s.search([2, 5, 6, 0, 0, 1, 2], 0) is True
    # Sample 2: target absent.
    assert s.search([2, 5, 6, 0, 0, 1, 2], 3) is False
    # All duplicates, target present / absent.
    assert s.search([1, 1, 1, 1, 1], 1) is True
    assert s.search([1, 1, 1, 1, 1], 2) is False
    # No rotation, and single element.
    assert s.search([1, 2, 3, 4, 5], 4) is True
    assert s.search([1], 1) is True
    assert s.search([1], 0) is False
    # Duplicates around the pivot.
    assert s.search([1, 0, 1, 1, 1], 0) is True
    print("All sample checks passed.")
