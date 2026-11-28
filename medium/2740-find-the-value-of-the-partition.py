# LeetCode 2740. Find the Value of the Partition — Medium
# https://leetcode.com/problems/find-the-value-of-the-partition/
# Submission 2205225365 — Accepted, Python3
#
# My thinking: sort the array. In the best partition the two
# groups can be taken as a lower and an upper slice of the
# sorted array, so the value is just the gap between two
# neighbours — and the smallest such gap is the answer.
class Solution:
    def findValueOfPartition(self, nums: list[int]) -> int:
        nums.sort()
        return min(b - a for a, b in zip(nums, nums[1:]))
