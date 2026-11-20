# 4088. Difference Between Peaks and Valleys (Easy)
# https://leetcode.com/problems/difference-between-peaks-and-valleys/
# Submission 2200104156 — Accepted, Python3
class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        # My thinking: I look at every middle element
        # — a peak adds its value, a valley subtracts
        # it — and the difference is the answer.
        total = 0
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                total += nums[i]
            elif nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
                total -= nums[i]
        return total
