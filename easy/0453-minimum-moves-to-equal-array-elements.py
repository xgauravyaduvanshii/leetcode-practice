# LeetCode 453. Minimum Moves to Equal Array Elements — Easy
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
# Submission 2197477552 — Accepted, Python3
#
# My thinking: adding 1 to every element except one
# is the same as subtracting 1 from that one element.
# So the cheapest target is the smallest element,
# and the answer is just how much everything above
# it needs to come down.

class Solution:
    def minMoves(self, nums: list[int]) -> int:
        return sum(nums) - len(nums) * min(nums)
