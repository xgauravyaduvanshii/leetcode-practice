# LeetCode 395. Longest Substring with At Least K Repeating Characters — Medium
# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
# Submission 2198774150 — Accepted, Python3
#
# My thinking: any character appearing fewer than k
# times can never be part of the answer, so it
# splits the string. I solve each piece on its own
# and take the best — if no character is too rare,
# the whole string qualifies.

from collections import Counter


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        counts = Counter(s)
        for char, count in counts.items():
            if count < k:
                return max(
                    self.longestSubstring(part, k) for part in s.split(char)
                )
        return len(s)
