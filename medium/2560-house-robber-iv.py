# LeetCode 2560. House Robber IV — Medium
# https://leetcode.com/problems/house-robber-iv/
# Submission 2205068757 — Accepted, Python3
#
# My thinking: binary-search the capability. For a candidate cap,
# greedily rob every house worth at most cap (skipping its
# neighbour) — that takes the most houses possible, so if even
# that greedy count is below k, the cap is too small.
class Solution:
    def minCapability(self, nums: list[int], k: int) -> int:
        def can(cap):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= cap:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= k

        lo, hi = 1, max(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if can(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
