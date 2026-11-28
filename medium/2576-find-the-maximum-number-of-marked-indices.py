# LeetCode 2576. Find the Maximum Number of Marked Indices — Medium
# https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/
# Submission 2205081345 — Accepted, Python3
#
# My thinking: sort, then pair the smallest unmarked elements
# with partners from the larger half. Walking the larger half
# once and pairing whenever 2*small <= large is optimal — a
# small element that can pair should take the smallest large
# element that fits it. The small pointer must stay inside the
# first half: pairing two elements from the larger half would
# reuse an element already spent as a partner.
class Solution:
    def maxNumOfMarkedIndices(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        i = 0
        marked = 0
        for j in range(n // 2, n):
            if i < n // 2 and 2 * nums[i] <= nums[j]:
                marked += 2
                i += 1
        return marked
