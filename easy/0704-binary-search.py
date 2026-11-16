# LeetCode 704. Binary Search — Easy
# https://leetcode.com/problems/binary-search/
# Submission 2197518069 — Accepted, Python3
#
# My thinking: classic binary search. I look at the
# middle of the remaining range — if it is the
# target, I am done; if it is too small, the
# target must be on the right; if too big, on the
# left. If the range runs out, it is not there.

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
