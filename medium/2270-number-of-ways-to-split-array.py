# LeetCode 2270. Number of Ways to Split Array — Medium
# https://leetcode.com/problems/number-of-ways-to-split-array/
# Submission 2204609760 — Accepted, Python3
#
# My thinking: I only need one pass. The total sum is fixed, so as I
# walk left to right I keep a running left sum; the right sum is just
# total minus left. A split after position i is good when the left part
# is at least as big as the right part, so I count every i (except the
# last element, which cannot be a split point) where left >= total - left.
class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        total = sum(nums)
        left = 0
        ans = 0
        for i in range(len(nums) - 1):
            left += nums[i]
            if left >= total - left:
                ans += 1
        return ans
