# 3407. Substring Matching Pattern (Easy)
# https://leetcode.com/problems/substring-matching-pattern/
# Submission 2200013802 — Accepted, Python3
class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        # My thinking: the star can stand for anything,
        # so I only need the part before it to appear
        # somewhere in s, and the part after it to
        # appear somewhere later. Empty parts always
        # match.
        star = p.index("*")
        before = p[:star]
        after = p[star + 1:]
        start = s.find(before)
        if start == -1:
            return False
        return s.find(after, start + len(before)) != -1
