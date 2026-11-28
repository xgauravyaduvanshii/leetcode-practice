# LeetCode 2439. Minimize Maximum of Array — Medium
# https://leetcode.com/problems/minimize-maximum-of-array/
# Submission 2204945628 — Accepted, Python3
#
# My thinking: binary-search the answer. To test a limit, sweep
# from right to left carrying any excess over the limit to the left
# neighbour — operations only move value leftwards, so excess has
# nowhere else to go. The limit works when nothing is left over at
# the first element.
class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        def feasible(limit: int) -> bool:
            carry = 0
            for i in range(len(nums) - 1, 0, -1):
                total = nums[i] + carry
                if total > limit:
                    carry = total - limit
                else:
                    carry = 0
            return nums[0] + carry <= limit

        lo, hi = 0, max(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
