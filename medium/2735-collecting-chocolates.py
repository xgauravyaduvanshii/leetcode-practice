# LeetCode 2735. Collecting Chocolates — Medium
# https://leetcode.com/problems/collecting-chocolates/
# Submission 2205222217 — Accepted, Python3
#
# My thinking: after k rotations, each type can be bought at
# the cheapest of the k+1 positions it has visited, so keep a
# running minimum per type and add the rotation cost k*x. Try
# every k from 0 to n-1 and keep the cheapest total — rotating
# n times just returns to the start, so nothing more is gained.
class Solution:
    def minCost(self, nums: list[int], x: int) -> int:
        n = len(nums)
        cur = nums[:]
        ans = sum(cur)
        for k in range(1, n):
            for i in range(n):
                cur[i] = min(cur[i], nums[(i - k) % n])
            ans = min(ans, sum(cur) + k * x)
        return ans
