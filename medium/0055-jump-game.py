# LeetCode 55. Jump Game — Medium
# https://leetcode.com/problems/jump-game/
# Submission 2203829767 — Accepted, Python3
#
# My thinking: I walk the array once, tracking the farthest index I
# can reach from everything seen so far. If I ever arrive at an index
# beyond that reach, the end is unreachable; if the reach covers the
# last index, I can make it. I never need to remember which jumps I
# took, only how far I can get.

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        reach = 0
        for i, jump in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, i + jump)
            if reach >= len(nums) - 1:
                return True
        return True
