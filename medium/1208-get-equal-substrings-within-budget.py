# LeetCode 1208. Get Equal Substrings Within Budget — Medium
# https://leetcode.com/problems/get-equal-substrings-within-budget/
# Submission 2199012450 — Accepted, Python3
#
# My thinking: I slide a window across the
# strings, paying the letter-change cost as it
# grows. When the cost passes the budget I
# shrink the window from the left until it fits
# again, and keep the widest window seen.

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        cost = 0
        best = 0
        for right, (a, b) in enumerate(zip(s, t)):
            cost += abs(ord(a) - ord(b))
            while cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            best = max(best, right - left + 1)
        return best
