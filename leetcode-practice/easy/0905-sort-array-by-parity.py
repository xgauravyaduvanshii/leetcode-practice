# LeetCode 905. Sort Array By Parity — Easy
# https://leetcode.com/problems/sort-array-by-parity/
# Submission 2197541020 — Accepted, Python3
#
# My thinking: two pointers, one from each end. The
# left one moves past evens (already in the right
# place) and the right one moves past odds. When
# they stop, the left points at an odd and the
# right at an even — I swap them and carry on.

class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] % 2 == 0:
                left += 1
            elif nums[right] % 2 == 1:
                right -= 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return nums
