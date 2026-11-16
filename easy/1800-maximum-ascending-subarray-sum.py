# LeetCode 1800. Maximum Ascending Subarray Sum — Easy
# https://leetcode.com/problems/maximum-ascending-subarray-sum/
# Submission 2197599006 — Accepted, Python3
#
# My thinking: I walk the array keeping the sum of
# the current ascending run. As long as each number
# is bigger than the one before it, I add it to the
# run; otherwise I start a fresh run at that number.
# The biggest run sum I ever see is the answer.

class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        best = cur = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur += nums[i]
            else:
                cur = nums[i]
            best = max(best, cur)
        return best
