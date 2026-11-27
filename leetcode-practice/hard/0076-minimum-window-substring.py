# LeetCode 76. Minimum Window Substring — Hard
# https://leetcode.com/problems/minimum-window-substring/
# Submission 2198381922 — Accepted, Python3
#
# My thinking: I grow a window from the right until
# it holds every letter of t, counting how many are
# still missing. Then I shrink it from the left as
# far as I can without losing a needed letter, and
# note the window if it is the shortest so far.
# Each end of the window only moves forward, so
# the whole scan is one pass.

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        left = 0
        best = (0, float("inf"))
        for right, ch in enumerate(s):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1
            while missing == 0:
                if right - left < best[1] - best[0]:
                    best = (left, right)
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1
        lo, hi = best
        return "" if hi == float("inf") else s[lo:hi + 1]
