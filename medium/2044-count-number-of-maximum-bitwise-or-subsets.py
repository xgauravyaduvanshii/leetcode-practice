# LeetCode 2044. Count Number of Maximum Bitwise-OR Subsets — Medium
# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/
# Submission 2204377521 — Accepted, Python3
#
# My thinking: the biggest OR any subset can reach is the OR of all the
# numbers, so I compute that target first and then simply count the
# non-empty subsets whose OR equals it. With at most 16 numbers there
# are only 65535 subsets, so enumerating every bitmask is fast enough.
class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        target = 0
        for x in nums:
            target |= x
        n = len(nums)
        count = 0
        for mask in range(1, 1 << n):
            orv = 0
            for i in range(n):
                if mask >> i & 1:
                    orv |= nums[i]
            if orv == target:
                count += 1
        return count
