# LeetCode 153. Find Minimum in Rotated Sorted Array — Medium
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Submission 2204051030 — Accepted, Python3
#
# My thinking: the array was sorted ascending and then rotated, so
# the smallest element is the one place where the order drops — the
# pivot. I binary search for it: at each step I compare the middle
# element with the rightmost one. If nums[mid] is bigger than
# nums[right], the pivot must be to the right of mid, so I move left
# to mid + 1. Otherwise the minimum is at mid or to its left, so I
# move right to mid. When the window closes to one element, that
# element is the minimum. If the array was never rotated, the loop
# still ends at the first element, which is correct.

class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


if __name__ == "__main__":
    sol = Solution()
    assert sol.findMin([3, 4, 5, 1, 2]) == 1
    assert sol.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert sol.findMin([11, 13, 15, 17]) == 11
    assert sol.findMin([2, 1]) == 1
    assert sol.findMin([1]) == 1
    print("All samples pass")
