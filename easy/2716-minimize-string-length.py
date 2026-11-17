# LeetCode 2716. Minimize String Length — Easy
# https://leetcode.com/problems/minimize-string-length/
# Submission 2197820397 — Accepted, Python3
#
# My thinking: I can delete one of any two equal
# characters, so eventually each distinct character
# appears exactly once. The shortest possible length
# is just the number of distinct characters.

class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))
