# LeetCode 976. Largest Perimeter Triangle — Easy
# https://leetcode.com/problems/largest-perimeter-triangle/
# Submission 2197547095 — Accepted, Python3
#
# My thinking: I sort the sides biggest first. The
# biggest triangle will use the biggest sides, so
# I check triples from the top down — the first
# triple where the biggest side is smaller than
# the other two put together is a real triangle,
# and it has the largest possible perimeter.

class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0
