# LeetCode 2134. Minimum Swaps to Group All 1's Together II — Medium
# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/
# Submission 2204469621 — Accepted, Python3
#
# My thinking: the 1's must end up in one block of length k, where k is
# the total number of 1's, and the array is circular. Every 0 inside that
# block has to be swapped out, so the answer is k minus the most 1's any
# length-k circular window already holds. I slide a window of size k
# around the circle and keep the best count.
class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        k = sum(nums)
        if k <= 1:
            return 0
        n = len(nums)
        cur = sum(nums[:k])
        max_ones = cur
        for i in range(1, n):
            cur += nums[(i + k - 1) % n] - nums[i - 1]
            if cur > max_ones:
                max_ones = cur
        return k - max_ones
