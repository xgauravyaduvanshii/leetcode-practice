# LeetCode 2302. Count Subarrays With Score Less Than K — Hard
# https://leetcode.com/problems/count-subarrays-with-score-less-than-k/
# Submission 2201666880 — Accepted, Python3
#
# My thinking: every number is positive,
# so a window's score only grows as it
# widens — I slide the right edge out and
# pull the left edge in until the score
# fits, and every start the window still
# covers is one more good subarray.

class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        total = 0
        window = 0
        left = 0
        for right, x in enumerate(nums):
            window += x
            while window * (right - left + 1) >= k:
                window -= nums[left]
                left += 1
            total += right - left + 1
        return total
