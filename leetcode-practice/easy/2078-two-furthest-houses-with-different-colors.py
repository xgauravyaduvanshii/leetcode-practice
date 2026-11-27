# LeetCode 2078. Two Furthest Houses With Different Colors — Easy
# https://leetcode.com/problems/two-furthest-houses-with-different-colors/
# Submission 2197611988 — Accepted, Python3
#
# My thinking: the farthest pair must use one of the
# ends. So I try two candidates: the first house
# from the left whose colour differs from the last
# house, and the first house from the right whose
# colour differs from the first house. The bigger of
# the two distances wins.

class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        n = len(colors)
        left = 0
        while colors[left] == colors[n - 1]:
            left += 1
        right = n - 1
        while colors[right] == colors[0]:
            right -= 1
        return max(n - 1 - left, right)
