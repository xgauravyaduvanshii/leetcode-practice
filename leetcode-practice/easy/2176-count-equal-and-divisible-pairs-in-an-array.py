# LeetCode 2176. Count Equal and Divisible Pairs in an Array — Easy
# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/
# Submission 2197616371 — Accepted, Python3
#
# My thinking: I check every pair of positions and
# count the ones where the values are equal and the
# product of the two indices is divisible by k.

class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    count += 1
        return count
