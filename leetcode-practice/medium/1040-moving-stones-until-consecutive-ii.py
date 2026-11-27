# LeetCode 1040. Moving Stones Until Consecutive II — Medium
# https://leetcode.com/problems/moving-stones-until-consecutive-ii/
# Submission 2198992371 — Accepted, Python3
#
# My thinking: for the maximum I count the empty
# spaces and subtract the bigger end gap, since
# one end can never be filled. For the minimum I
# slide a window over the sorted stones — the
# most stones already inside one window of the
# right size is the most I can keep. One trap:
# when n minus 1 stones are already consecutive,
# it still takes two moves unless the odd stone
# sits exactly two away, when moving the far end
# of the block into the gap finishes it in one.

from typing import List


class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        n = len(stones)
        max_moves = stones[-1] - stones[0] + 1 - n - min(
            stones[1] - stones[0] - 1, stones[-1] - stones[-2] - 1
        )
        min_moves = n
        left = 0
        for right in range(n):
            while stones[right] - stones[left] + 1 > n:
                left += 1
            count = right - left + 1
            if count == n - 1 and stones[right] - stones[left] == n - 2:
                if left > 0 and stones[left] - stones[left - 1] == 2:
                    min_moves = min(min_moves, 1)
                elif right + 1 < n and stones[right + 1] - stones[right] == 2:
                    min_moves = min(min_moves, 1)
                else:
                    min_moves = min(min_moves, 2)
            else:
                min_moves = min(min_moves, n - count)
        return [min_moves, max_moves]
