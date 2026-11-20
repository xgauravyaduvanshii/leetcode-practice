# LeetCode 1630. Arithmetic Subarrays — Medium
# https://leetcode.com/problems/arithmetic-subarrays/
# Submission 2199895273 — Accepted, Python3
#
# My thinking: a subarray is arithmetic when
# its sorted values step by the same amount
# throughout. I sort each query's slice and
# check the gaps one by one.

from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def is_arithmetic(sub):
            if len(sub) <= 2:
                return True
            sub.sort()
            diff = sub[1] - sub[0]
            return all(sub[i] - sub[i - 1] == diff for i in range(2, len(sub)))

        return [is_arithmetic(nums[left:right + 1]) for left, right in zip(l, r)]
