# LeetCode 2420. Find All Good Indices — Medium
# https://leetcode.com/problems/find-all-good-indices/
# Submission 2204860240 — Accepted, Python3
#
# My thinking: precompute, for each index, how long the non-increasing
# run ending there is and how long the non-decreasing run starting
# there is. Index i is good when the k elements before it are
# non-increasing (left run at i-1 >= k) and the k after it are
# non-decreasing (right run at i+1 >= k).
from typing import List


class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        left = [1] * n
        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                left[i] = left[i - 1] + 1
        right = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                right[i] = right[i + 1] + 1
        return [i for i in range(k, n - k) if left[i - 1] >= k and right[i + 1] >= k]
