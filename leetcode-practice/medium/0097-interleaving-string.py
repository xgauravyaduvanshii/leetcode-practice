# LeetCode 97. Interleaving String — Medium
# https://leetcode.com/problems/interleaving-string/
# Submission 2200952395 — Accepted, Python3
#
# My thinking: I walk through both strings at once,
# keeping the set of positions I could have reached —
# a position is reachable if the next letter of either
# string matches the next letter of the target.

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        reachable = {0}
        for i, ch in enumerate(s3):
            nxt = set()
            for j in reachable:
                if j < len(s1) and s1[j] == ch:
                    nxt.add(j + 1)
                if i - j < len(s2) and s2[i - j] == ch:
                    nxt.add(j)
            reachable = nxt
            if not reachable:
                return False
        return len(s1) in reachable
