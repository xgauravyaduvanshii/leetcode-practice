# LeetCode 2210. Count Hills and Valleys in an Array — Easy
# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/
# Submission 2197618063 — Accepted, Python3
#
# My thinking: flat stretches don't change the shape,
# so I first squeeze out consecutive duplicates.
# Then a position is a hill when it is higher than
# both neighbours, and a valley when it is lower
# than both.

class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        a = [nums[0]]
        for x in nums[1:]:
            if x != a[-1]:
                a.append(x)
        count = 0
        for i in range(1, len(a) - 1):
            if (a[i] > a[i - 1] and a[i] > a[i + 1]) or (a[i] < a[i - 1] and a[i] < a[i + 1]):
                count += 1
        return count
