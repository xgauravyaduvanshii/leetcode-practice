# LeetCode 31. Next Permutation — Medium
# https://leetcode.com/problems/next-permutation/
# Submission 2203815305 — Accepted, Python3
#
# My thinking: I scan from the right for the first position where the
# number rises — everything after it is falling, so it is the largest
# arrangement of that tail. I swap that position with the smallest
# number after it that is still bigger than it, then reverse the tail
# to make it the smallest possible. If nothing rises, the whole array
# is already the largest, so reversing it gives the smallest.

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        n = len(nums)
        pivot = n - 2
        while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
            pivot -= 1
        if pivot >= 0:
            swap = n - 1
            while nums[swap] <= nums[pivot]:
                swap -= 1
            nums[pivot], nums[swap] = nums[swap], nums[pivot]
        left, right = pivot + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
