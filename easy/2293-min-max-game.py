# LeetCode 2293. Min Max Game — Easy
# https://leetcode.com/problems/min-max-game/
# Submission 2197621827 — Accepted, Python3
#
# My thinking: each round I pair up the numbers and
# keep the smaller one for even pairs and the bigger
# one for odd pairs. I repeat until one number is
# left.

class Solution:
    def minMaxGame(self, nums: list[int]) -> int:
        while len(nums) > 1:
            nxt = []
            for i in range(len(nums) // 2):
                if i % 2 == 0:
                    nxt.append(min(nums[2 * i], nums[2 * i + 1]))
                else:
                    nxt.append(max(nums[2 * i], nums[2 * i + 1]))
            nums = nxt
        return nums[0]
