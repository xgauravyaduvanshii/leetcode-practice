# LeetCode 2138. Divide a String Into Groups of Size k — Easy
# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/
# Submission 2197614576 — Accepted, Python3
#
# My thinking: I cut the string into chunks of size
# k. If the last chunk is short, I pad it with the
# fill character until it reaches size k.

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        groups = [s[i:i + k] for i in range(0, len(s), k)]
        groups[-1] = groups[-1] + fill * (k - len(groups[-1]))
        return groups
