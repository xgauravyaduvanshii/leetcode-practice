# LeetCode 424. Longest Repeating Character Replacement — Medium
# https://leetcode.com/problems/longest-repeating-character-replacement/
# Submission 2198787250 — Accepted, Python3
#
# My thinking: a window works when the letters that
# are not the most common one inside it fit within
# k replacements. I grow the window and only shrink
# it from the left when that stops being true, and
# the widest window I ever see is the answer.

from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = Counter()
        left = 0
        best = 0
        for right, char in enumerate(s):
            counts[char] += 1
            while (right - left + 1) - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best
