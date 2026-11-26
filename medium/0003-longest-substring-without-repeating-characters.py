# LeetCode 3. Longest Substring Without Repeating Characters — Medium
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Submission 2203750647 — Accepted, Python3
#
# My thinking: I slide a window over the string, remembering the
# last index where each character was seen. When a repeat shows up
# inside the current window, I move the left edge to just past that
# character's previous spot, so the window never holds a duplicate.
# The best window length seen is the answer.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        left = 0
        best = 0
        for right, ch in enumerate(s):
            if ch in last and last[ch] >= left:
                left = last[ch] + 1
            last[ch] = right
            if right - left + 1 > best:
                best = right - left + 1
        return best
