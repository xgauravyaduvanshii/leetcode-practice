# LeetCode 1234. Replace the Substring for Balanced String — Medium
# https://leetcode.com/problems/replace-the-substring-for-balanced-string/
# Submission 2199016877 — Accepted, Python3
#
# My thinking: a balanced string needs each
# letter exactly a quarter of the time. I slide
# a window and shrink it while the letters
# outside it are all within their quota — the
# smallest such window is the answer.

from collections import Counter


class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        target = n // 4
        counts = Counter(s)
        if all(counts[ch] <= target for ch in "QWER"):
            return 0
        best = n
        left = 0
        for right, ch in enumerate(s):
            counts[ch] -= 1
            while all(counts[c] <= target for c in "QWER"):
                best = min(best, right - left + 1)
                counts[s[left]] += 1
                left += 1
        return best
