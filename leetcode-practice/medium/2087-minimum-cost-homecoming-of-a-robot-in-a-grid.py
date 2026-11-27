# LeetCode 2087. Minimum Cost Homecoming of a Robot in a Grid — Medium
# https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/
# Submission 2204401824 — Accepted, Python3
#
# My thinking: the robot only has to move from its start row to the
# home row and from its start column to the home column, and every
# row or column it enters costs exactly that row's or column's price
# once. The order of the moves does not matter, so the answer is just
# the sum of the row costs crossed plus the sum of the column costs
# crossed.
class Solution:
    def minCost(self, startPos: list[int], homePos: list[int], rowCosts: list[int], colCosts: list[int]) -> int:
        sr, sc = startPos
        hr, hc = homePos
        total = 0
        if sr < hr:
            total += sum(rowCosts[sr + 1:hr + 1])
        elif sr > hr:
            total += sum(rowCosts[hr:sr])
        if sc < hc:
            total += sum(colCosts[sc + 1:hc + 1])
        elif sc > hc:
            total += sum(colCosts[hc:sc])
        return total
