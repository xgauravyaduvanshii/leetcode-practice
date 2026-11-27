# LeetCode 2295. Replace Elements in an Array — Medium
# https://leetcode.com/problems/replace-elements-in-an-array/
# Submission 2204657422 — Accepted, Python3
#
# My thinking: keep a map from each value to its index. Each operation
# then takes O(1): look up where the old value sits, write the new value
# there, and move the map entry from the old value to the new one. The
# array itself is updated in place, so the final array is the answer.
class Solution:
    def arrayChange(self, nums: list[int], operations: list[list[int]]) -> list[int]:
        pos = {v: i for i, v in enumerate(nums)}
        for old, new in operations:
            i = pos.pop(old)
            nums[i] = new
            pos[new] = i
        return nums
