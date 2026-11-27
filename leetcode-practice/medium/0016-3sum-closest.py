# LeetCode 16. 3Sum Closest — Medium
# https://leetcode.com/problems/3sum-closest/
# Submission 2200889461 — Accepted, Python3
#
# My thinking:
# Sort the array first so we can move pointers inward based on how the
# current sum compares to the target.
# Fix one number at index i, then use two pointers (left just after i,
# right at the end) to pick the other two. The three together form a
# candidate sum.
# After each candidate, check how close it is to the target and keep the
# closest one seen so far. If the candidate equals the target exactly,
# it cannot be beaten, so return it right away.
# If the candidate sum is smaller than the target, move the left pointer
# right to try a larger sum; if it is larger, move the right pointer left
# to try a smaller sum. Because the array is sorted, this explores the
# useful pairs for each fixed i in linear time.

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        n = len(nums)

        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(total - target) < abs(closest - target):
                    closest = total
                if total == target:
                    return total
                elif total < target:
                    left += 1
                else:
                    right -= 1

        return closest
