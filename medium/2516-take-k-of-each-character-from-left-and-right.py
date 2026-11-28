# LeetCode 2516. Take K of Each Character From Left and Right — Medium
# https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/
# Submission 2204980984 — Accepted, Python3
#
# My thinking: if any of a, b, c appears fewer than k times, the
# task is impossible. Otherwise find the longest middle window we
# can leave untouched — it may hold at most total minus k of each
# character — and take everything outside it. The shortest take is
# the string length minus that longest window.
from collections import Counter


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        total = Counter(s)
        if any(total[c] < k for c in "abc"):
            return -1
        limit = {c: total[c] - k for c in "abc"}
        n = len(s)
        window = Counter()
        left = 0
        best = 0
        for right, ch in enumerate(s):
            window[ch] += 1
            while window[ch] > limit[ch]:
                window[s[left]] -= 1
                left += 1
            best = max(best, right - left + 1)
        return n - best
