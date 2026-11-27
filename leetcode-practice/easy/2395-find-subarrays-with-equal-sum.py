# LeetCode 2395. Find Subarrays With Equal Sum — Easy
# https://leetcode.com/problems/find-subarrays-with-equal-sum/
# Submission 2197777834 — Accepted, Python3
#
# My thinking: I look at the sum of every pair of
# adjacent numbers. If any sum appears twice, two
# subarrays have the same sum.

class Solution:
    def findSubarrays(self, nums: list[int]) -> bool:
        seen = set()
        for i in range(len(nums) - 1):
            s = nums[i] + nums[i + 1]
            if s in seen:
                return True
            seen.add(s)
        return False
