# 3925. Concatenate Array With Reverse (Easy)
# https://leetcode.com/problems/concatenate-array-with-reverse/
# Submission 2200088224 — Accepted, Python3
class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        # My thinking: the answer is the array itself
        # followed by the same array read backwards.
        return nums + nums[::-1]
