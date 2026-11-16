# LeetCode 977. Squares of a Sorted Array — Easy
# https://leetcode.com/problems/squares-of-a-sorted-array/
# Submission 2197547498 — Accepted, Python3
#
# My thinking: after squaring, the biggest values
# come from the ends of the array (the most
# negative or the most positive). So I compare the
# two ends, put the bigger square at the back of
# the answer, and work my way inwards.

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        pos = n - 1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[pos] = nums[left] * nums[left]
                left += 1
            else:
                result[pos] = nums[right] * nums[right]
                right -= 1
            pos -= 1
        return result
