# LeetCode 167. Two Sum II - Input Array Is Sorted — Medium
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Submission 2198435776 — Accepted, Python3
#
# My thinking: with the array sorted, I take one
# number from each end. If the pair is too small I
# move the left end up; if it is too big I move the
# right end down. The pair that hits the target is
# the answer, and the problem counts positions
# from one.

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            if total < target:
                left += 1
            else:
                right -= 1
        return []
