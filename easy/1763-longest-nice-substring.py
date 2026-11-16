# LeetCode 1763. Longest Nice Substring — Easy
# https://leetcode.com/problems/longest-nice-substring/
# Submission 2197597427 — Accepted, Python3
#
# My thinking: a substring is nice when every letter
# appears in both cases. If some letter in the
# string lacks its opposite case, it splits the
# string — the answer must lie entirely to its left
# or entirely to its right, so I recurse on both
# sides and keep the longer one.

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        chars = set(s)
        for i, ch in enumerate(s):
            if ch.swapcase() not in chars:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i + 1:])
                return left if len(left) >= len(right) else right
        return s
