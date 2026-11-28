# LeetCode 2498. Frog Jump II — Medium
# https://leetcode.com/problems/frog-jump-ii/
# Submission 2204974655 — Accepted, Python3
#
# My thinking: the frog must cross every gap twice — once on the way
# out and once on the way back — except it can skip one stone in
# each direction by jumping over it. So the widest jump it cannot
# avoid is the largest distance between stones two apart (and the
# first gap, which has no stone to skip over).
class Solution:
    def maxJump(self, stones: list[int]) -> int:
        res = stones[1] - stones[0]
        for i in range(len(stones) - 2):
            res = max(res, stones[i + 2] - stones[i])
        return res
