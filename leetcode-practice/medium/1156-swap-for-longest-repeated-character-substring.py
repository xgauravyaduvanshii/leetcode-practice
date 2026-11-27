# LeetCode 1156. Swap For Longest Repeated Character Substring — Medium
# https://leetcode.com/problems/swap-for-longest-repeated-character-substring/
# Submission 2199008313 — Accepted, Python3
#
# My thinking: I read the string as runs of the
# same letter. A run can grow by one with a swap
# if that letter appears elsewhere, and two runs
# separated by a single different letter can
# join into one.

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        groups = []
        for ch in text:
            if groups and groups[-1][0] == ch:
                groups[-1][1] += 1
            else:
                groups.append([ch, 1])
        totals = {}
        for ch, count in groups:
            totals[ch] = totals.get(ch, 0) + count
        best = 0
        for i, (ch, count) in enumerate(groups):
            extra = 1 if totals[ch] > count else 0
            best = max(best, count + extra)
            if 0 < i < len(groups) - 1 and groups[i - 1][0] == groups[i + 1][0] and groups[i][1] == 1:
                merged = groups[i - 1][1] + groups[i + 1][1]
                extra = 1 if totals[groups[i - 1][0]] > merged else 0
                best = max(best, merged + extra)
        return best
