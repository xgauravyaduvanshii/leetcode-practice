# LeetCode 287. Find the Duplicate Number — Medium
# https://leetcode.com/problems/find-the-duplicate-number/
# Submission 2198733830 — Accepted, Python3
#
# My thinking: each value points at the next index,
# so the array hides a linked list with a cycle, and
# the duplicate is where the cycle begins. Two
# pointers meet inside the cycle, then one restarts
# from the start — they meet again at the duplicate.

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
