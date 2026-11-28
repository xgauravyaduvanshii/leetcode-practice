# LeetCode 2483. Minimum Penalty for a Shop — Medium
# https://leetcode.com/problems/minimum-penalty-for-a-shop/
# Submission 2204971855 — Accepted, Python3
#
# My thinking: closing at hour 0 costs one penalty per 'Y' in the
# whole string. Walk the hours left to right: passing a 'Y' removes
# a penalty (it is now served), passing an 'N' adds one (the shop
# stayed open for nobody). The hour with the lowest running penalty
# is the best closing time.
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = customers.count('Y')
        best = 0
        best_penalty = penalty
        for i, ch in enumerate(customers):
            if ch == 'Y':
                penalty -= 1
            else:
                penalty += 1
            if penalty < best_penalty:
                best_penalty = penalty
                best = i + 1
        return best
