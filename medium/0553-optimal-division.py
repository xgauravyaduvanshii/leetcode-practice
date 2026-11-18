# LeetCode 553. Optimal Division — Medium
# https://leetcode.com/problems/optimal-division/
# Submission 2198861854 — Accepted, Python3
#
# My thinking: the first number should stay on top
# and every number after it should divide the next
# one, so grouping all of them after the first in
# one bracket makes the result as large as it can
# be.

from typing import List


class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return f"{nums[0]}/{nums[1]}"
        return str(nums[0]) + "/(" + "/".join(str(num) for num in nums[1:]) + ")"
