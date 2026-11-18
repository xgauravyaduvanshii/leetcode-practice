# LeetCode 780. Reaching Points — Hard
# https://leetcode.com/problems/reaching-points/
# Submission 2198675712 — Accepted, Python3
#
# My thinking: walking forward from the start would
# take forever, so I walk backwards from the target
# instead. Each step back subtracts the smaller
# number from the bigger one — in bulk, with a modulo
# — until one coordinate meets the start. Then the
# other one just has to reach the start in whole
# steps of the first.

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx > sx and ty > sy and tx != ty:
            if tx > ty:
                tx %= ty
            else:
                ty %= tx
        if tx == sx and ty == sy:
            return True
        if tx == sx:
            return ty > sy and (ty - sy) % tx == 0
        if ty == sy:
            return tx > sx and (tx - sx) % ty == 0
        return False
