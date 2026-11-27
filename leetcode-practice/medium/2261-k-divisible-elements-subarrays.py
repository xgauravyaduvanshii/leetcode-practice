# LeetCode 2261. K Divisible Elements Subarrays — Medium
# https://leetcode.com/problems/k-divisible-elements-subarrays/
# Submission 2204519789 — Accepted, Python3
#
# My thinking: I enumerate every subarray starting at each index,
# stopping as soon as it holds more than k elements divisible by p.
# Each subarray is added to a set as a tuple, so identical subarrays
# from different positions collapse into one entry, and the set size is
# the number of distinct valid subarrays.
class Solution:
    def countDistinct(self, nums: list[int], k: int, p: int) -> int:
        n = len(nums)
        seen = set()
        for i in range(n):
            cnt = 0
            for j in range(i, n):
                if nums[j] % p == 0:
                    cnt += 1
                if cnt > k:
                    break
                seen.add(tuple(nums[i:j + 1]))
        return len(seen)
