# 3114. Latest Time You Can Obtain After Replacing Characters (Easy)
# https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/
# Submission 2199978099 — Accepted, Python3
class Solution:
    def findLatestTime(self, s: str) -> str:
        # My thinking: fill each '?' with the biggest
        # digit that still keeps a valid time. The first
        # hour digit depends on the second one, and the
        # first minute digit can never pass 5.
        chars = list(s)
        if chars[0] == "?":
            chars[0] = "1" if chars[1] in "?01" else "0"
        if chars[1] == "?":
            chars[1] = "1" if chars[0] == "1" else "9"
        if chars[3] == "?":
            chars[3] = "5"
        if chars[4] == "?":
            chars[4] = "9"
        return "".join(chars)
