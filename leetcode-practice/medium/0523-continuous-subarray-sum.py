# LeetCode 523. Continuous Subarray Sum — Medium
# https://leetcode.com/problems/continuous-subarray-sum/
# Submission 2198845359 — Accepted, Python3
#
# My thinking: a subarray sum is a multiple of k
# exactly when two running totals share the same
# remainder. I remember the first place each
# remainder appeared and check that the two
# positions are at least two apart.

from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        seen = {0: -1}
        running = 0
        for i, num in enumerate(nums):
            running += num
            remainder = running % k
            if remainder in seen:
                if i - seen[remainder] >= 2:
                    return True
            else:
                seen[remainder] = i
        return False
