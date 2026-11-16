# LeetCode 53. Maximum Subarray — Medium
# https://leetcode.com/problems/maximum-subarray/
# Submission 2197383338 — Accepted, Python3
#
# My thinking: at each number I decide whether to extend
# the subarray I am carrying or start fresh here. I keep
# the best sum I have seen so far — that is Kadane's idea.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algorithm: keep the best sum ending at each position.
        best = current = nums[0]
        for num in nums[1:]:
            # Either extend the running subarray or start fresh at num.
            current = max(num, current + num)
            best = max(best, current)
        return best
