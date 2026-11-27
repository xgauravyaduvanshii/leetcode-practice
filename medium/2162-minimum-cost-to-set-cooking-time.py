# LeetCode 2162. Minimum Cost to Set Cooking Time — Medium
# https://leetcode.com/problems/minimum-cost-to-set-cooking-time/
# Submission 2204482276 — Accepted, Python3
#
# My thinking: the target seconds can be written as minutes and seconds
# in several ways (mm from 0 to 99, ss = target - 60*mm, also 0 to 99),
# and each way can be typed with 1 to 4 digits by dropping leading
# zeros. I try every valid (mm, ss) pair and every allowed digit length,
# price each keystroke sequence from the starting digit, and keep the
# cheapest total.
class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def cost(digits):
            cur = startAt
            total = 0
            for ch in digits:
                d = int(ch)
                if d != cur:
                    total += moveCost
                    cur = d
                total += pushCost
            return total
        best = float('inf')
        for mm in range(100):
            ss = targetSeconds - 60 * mm
            if ss < 0 or ss > 99:
                continue
            s = f"{mm:02d}{ss:02d}"
            for k in range(1, 5):
                if s[:4 - k] != '0' * (4 - k):
                    continue
                best = min(best, cost(s[4 - k:]))
        return best
