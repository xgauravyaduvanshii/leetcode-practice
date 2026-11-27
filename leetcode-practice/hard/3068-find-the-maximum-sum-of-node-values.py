# LeetCode 3068. Find the Maximum Sum of Node Values — Hard
# https://leetcode.com/problems/find-the-maximum-sum-of-node-values/
# Submission 2201919603 — Accepted, Python3
#
# My thinking: every operation flips two
# nodes at once, so the flipped nodes
# must come in pairs — any even-sized
# set can be flipped, and no odd-sized
# set can. So I take every node where
# flipping gains value, and if that
# leaves an odd count, I give back the
# smallest gain (or take the smallest
# loss) to make the count even.

from typing import List


class Solution:
    def maximumValueSum(
        self, nums: List[int], k: int, edges: List[List[int]]
    ) -> int:
        total = sum(nums)
        gain_sum = 0
        flips = 0
        smallest_loss = 10**18
        for x in nums:
            gain = (x ^ k) - x
            if gain > 0:
                gain_sum += gain
                flips += 1
            smallest_loss = min(smallest_loss, abs(gain))
        if flips % 2 == 1:
            gain_sum -= smallest_loss
        return total + gain_sum
