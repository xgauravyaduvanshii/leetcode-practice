# LeetCode 1619. Mean of Array After Removing Some Elements — Easy
# https://leetcode.com/problems/mean-of-array-after-removing-some-elements/
# Submission 2197589665 — Accepted, Python3
#
# My thinking: I sort the array and cut off the
# smallest 5% and the largest 5% — that is
# len // 20 from each end. Then I average what
# is left.

class Solution:
    def trimMean(self, arr: list[int]) -> float:
        arr.sort()
        k = len(arr) // 20
        trimmed = arr[k:len(arr) - k]
        return sum(trimmed) / len(trimmed)
