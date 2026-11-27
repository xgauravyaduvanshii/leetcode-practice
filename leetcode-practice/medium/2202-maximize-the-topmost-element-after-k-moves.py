# LeetCode 2202. Maximize the Topmost Element After K Moves — Medium
# https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/
# Submission 2204498350 — Accepted, Python3
#
# My thinking: after k moves the top is either an element I popped off
# and put back, or the element k positions down that I never touched.
# With a single element, popping it k times returns it only when k is
# even. Otherwise the best popped candidate comes from the first k-1
# elements (the ones I can reach and return), and the untouched
# candidate is nums[k] when it exists.
class Solution:
    def maximumTop(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return nums[0] if k % 2 == 0 else -1
        ans = -1
        if k > 1:
            ans = max(ans, max(nums[:min(k - 1, n)]))
        if k < n:
            ans = max(ans, nums[k])
        return ans
