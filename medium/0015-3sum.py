# LeetCode 15. 3Sum — Medium
# https://leetcode.com/problems/3sum/
# Submission 2203805209 — Accepted, Python3
#
# My thinking: I sort the numbers, then fix the first element of each
# triplet and find the other two with two pointers moving in from the
# ends. Skipping equal neighbours at every step keeps duplicate
# triplets out, and the sorted order tells me which pointer to move:
# too small a sum, move left up; too big, move right down.

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return ans
