# LeetCode 457. Circular Array Loop — Medium
# https://leetcode.com/problems/circular-array-loop/
# Submission 2198807515 — Accepted, Python3
#
# My thinking: from each starting index I run a
# slow and a fast pointer around the circle. Both
# must keep moving in the starting direction, and a
# step that stays in place is not a loop. If the
# fast pointer ever laps the slow one, a real cycle
# exists.

from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        for start in range(n):
            if nums[start] == 0:
                continue
            slow = fast = start
            while True:
                slow = next_index(slow)
                if nums[slow] * nums[start] <= 0 or slow == next_index(slow):
                    break
                fast = next_index(fast)
                if nums[fast] * nums[start] <= 0 or fast == next_index(fast):
                    break
                fast = next_index(fast)
                if nums[fast] * nums[start] <= 0 or fast == next_index(fast):
                    break
                if slow == fast:
                    return True
        return False
