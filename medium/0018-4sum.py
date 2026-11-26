# LeetCode 18. 4Sum — Medium
# https://leetcode.com/problems/4sum/
# Submission 2203806990 — Accepted, Python3
#
# My thinking: like 3Sum, I sort first and fix the first two numbers
# of each quadruplet, then find the last two with two pointers. I skip
# equal neighbours at both fixed positions and at both pointers, so no
# quadruplet is ever reported twice, and the sorted order tells me
# which pointer to move based on whether the sum is too small or big.

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
        return ans
