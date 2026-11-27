# LeetCode 2139. Minimum Moves to Reach Target Score — Medium
# https://leetcode.com/problems/minimum-moves-to-reach-target-score/
# Submission 2204471368 — Accepted, Python3
#
# My thinking: working backwards from the target is greedy and optimal:
# halving is always better than subtracting when it is available, so I
# halve on even targets while doubles remain and subtract 1 on odd
# ones. Once the doubles run out, the only move left is to decrement
# all the way down to 1.
class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        while target > 1:
            if maxDoubles == 0:
                moves += target - 1
                break
            if target % 2 == 0:
                target //= 2
                maxDoubles -= 1
                moves += 1
            else:
                target -= 1
                moves += 1
        return moves
