# LeetCode 2537. Count the Number of Good Subarrays — Medium
# https://leetcode.com/problems/count-the-number-of-good-subarrays/
# Submission 2205055104 — Accepted, Python3
#
# My thinking: slide a window and keep the number of equal pairs
# inside it. Adding a value creates as many new pairs as its
# current frequency. Once the window is good, every extension to
# the right is good too, so add len(nums) - right and shrink from
# the left until it stops being good.
from collections import defaultdict


class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        freq = defaultdict(int)
        pairs = 0
        left = 0
        ans = 0
        for right, x in enumerate(nums):
            pairs += freq[x]
            freq[x] += 1
            while pairs >= k:
                ans += len(nums) - right
                freq[nums[left]] -= 1
                pairs -= freq[nums[left]]
                left += 1
        return ans
