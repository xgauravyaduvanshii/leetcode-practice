# LeetCode 2028. Find Missing Observations — Medium
# https://leetcode.com/problems/find-missing-observations/
# Submission 2204147967 — Accepted, Python3
#
# My thinking: the missing rolls have to add up to a fixed
# total — mean times all n + m rolls, minus the rolls I can
# still see. If that total is less than n (every missing roll
# is at least 1) or more than 6 * n (every missing roll is at
# most 6), no answer exists and I return an empty list.
# Otherwise I spread the total as evenly as possible: every
# missing roll gets total // n, and the leftover remainder
# adds one extra to that many rolls, so each value stays
# between 1 and 6.

class Solution:
    def missingRolls(self, rolls, mean, n):
        missing_total = mean * (len(rolls) + n) - sum(rolls)
        if missing_total < n or missing_total > 6 * n:
            return []
        base, extra = divmod(missing_total, n)
        return [base + 1] * extra + [base] * (n - extra)
