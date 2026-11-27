# LeetCode 1389. Create Target Array in the Given Order — Easy
# https://leetcode.com/problems/create-target-array-in-the-given-order/
# Submission 2197575285 — Accepted, Python3
#
# My thinking: I build the target list one element at
# a time, inserting each number at the index given
# for it. Python's insert pushes the rest to the
# right, exactly like the problem describes.

class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        target = []
        for num, i in zip(nums, index):
            target.insert(i, num)
        return target
