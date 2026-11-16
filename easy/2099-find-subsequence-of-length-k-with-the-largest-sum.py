# LeetCode 2099. Find Subsequence of Length K With the Largest Sum — Easy
# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/
# Submission 2197612781 — Accepted, Python3
#
# My thinking: the largest sum comes from the k
# biggest numbers. I pick their indices, sort those
# indices back into their original order, and return
# the numbers in that order.

class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        indices = sorted(range(len(nums)), key=lambda i: nums[i], reverse=True)[:k]
        return [nums[i] for i in sorted(indices)]
