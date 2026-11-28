# LeetCode 2680. Maximum OR — Medium
# https://leetcode.com/problems/maximum-or/
# Submission 2205190222 — Accepted, Python3
#
# My thinking: putting all k doublings on one element is best,
# because shifting one number left by k can only add bits, while
# splitting the shifts across elements wastes them on bits the
# OR already has. So try each element as the boosted one: its
# value shifted left by k, OR-ed with the prefix OR before it
# and the suffix OR after it, and keep the maximum.
class Solution:
    def maximumOr(self, nums: list[int], k: int) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i, x in enumerate(nums):
            pre[i + 1] = pre[i] | x
        suf = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suf[i] = suf[i + 1] | nums[i]
        ans = 0
        for i, x in enumerate(nums):
            ans = max(ans, (x << k) | pre[i] | suf[i + 1])
        return ans
