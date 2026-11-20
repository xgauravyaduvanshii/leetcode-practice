# LeetCode 1558. Minimum Numbers of Function Calls to Make Target Array — Medium
# https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/
# Submission 2199876074 — Accepted, Python3
#
# My thinking: I build each number from zero
# in reverse — halving costs a shared doubling
# step, and every odd bit costs one increment.
# The doublings are shared across all numbers,
# so only the deepest one counts.

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        max_doubles = 0
        for value in nums:
            doubles = 0
            while value > 0:
                if value % 2 == 1:
                    operations += 1
                    value -= 1
                else:
                    value //= 2
                    doubles += 1
            max_doubles = max(max_doubles, doubles)
        return operations + max_doubles
