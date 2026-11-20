# LeetCode 1769. Minimum Number of Operations to Move All Balls to Each Box — Medium
# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
# Submission 2199932432 — Accepted, Python3
#
# My thinking: I sweep once from the left
# counting the balls I have passed and the
# steps they still need, then once from the
# right. Each box's answer is the two sweeps
# added together.

from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        result = [0] * n
        balls = 0
        moves = 0
        for i in range(n):
            result[i] += moves
            if boxes[i] == "1":
                balls += 1
            moves += balls
        balls = 0
        moves = 0
        for i in range(n - 1, -1, -1):
            result[i] += moves
            if boxes[i] == "1":
                balls += 1
            moves += balls
        return result
