# 3912. Valid Elements in an Array (Easy)
# https://leetcode.com/problems/valid-elements-in-an-array/
# Submission 2200087153 — Accepted, Python3
class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        # My thinking: the first and last elements
        # always count. Any other element counts when
        # it beats everything on its left or everything
        # on its right.
        n = len(nums)
        out = []
        for i, x in enumerate(nums):
            if i == 0 or i == n - 1:
                out.append(x)
            elif x > max(nums[:i]) or x > max(nums[i + 1:]):
                out.append(x)
        return out
