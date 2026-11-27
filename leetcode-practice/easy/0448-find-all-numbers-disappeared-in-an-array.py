# LeetCode 448. Find All Numbers Disappeared in an Array — Easy
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Submission 2197476961 — Accepted, Python3
#
# My thinking: the numbers are supposed to be 1 to n,
# so I use the array itself as a checklist. For each
# number I see, I mark its position negative. At the
# end, the positions that are still positive were
# never marked — those numbers are missing.

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        return [i + 1 for i, num in enumerate(nums) if num > 0]
