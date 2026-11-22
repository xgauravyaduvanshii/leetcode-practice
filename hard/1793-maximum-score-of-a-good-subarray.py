# LeetCode 1793. Maximum Score of a Good Subarray — Hard
# https://leetcode.com/problems/maximum-score-of-a-good-subarray/
# Submission 2201167837 — Accepted, Python3
#
# My thinking: the subarray must contain k, so I
# grow out from k one step at a time, always
# reaching for the taller side first — that keeps
# the minimum as high as possible for as long as
# possible.

class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        n = len(nums)
        left = right = k
        cur_min = nums[k]
        best = nums[k]
        while left > 0 or right < n - 1:
            if right == n - 1 or (left > 0 and nums[left - 1] > nums[right + 1]):
                left -= 1
                cur_min = min(cur_min, nums[left])
            else:
                right += 1
                cur_min = min(cur_min, nums[right])
            best = max(best, cur_min * (right - left + 1))
        return best
