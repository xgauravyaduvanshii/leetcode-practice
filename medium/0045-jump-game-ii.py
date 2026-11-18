# LeetCode 45. Jump Game II — Medium
# https://leetcode.com/problems/jump-game-ii/
# Submission 2198431479 — Accepted, Python3
#
# My thinking: I walk the array once, keeping track
# of how far the current jump can reach and how far
# any jump from here can reach. Whenever I step past
# the end of the current jump's reach I have to take
# another jump, and its reach becomes the farthest
# I have seen. Each jump stretches as far as it can,
# so the count is the smallest possible.

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
        return jumps
