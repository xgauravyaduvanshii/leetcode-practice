# 3992. Rearrange String to Avoid Character Pair (Easy)
# https://leetcode.com/problems/rearrange-string-to-avoid-character-pair/
# Submission 2200093837 — Accepted, Python3
class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        # My thinking: I put every y first, then all
        # the other letters, then every x last — that
        # way no x can ever sit before a y.
        ys = [ch for ch in s if ch == y]
        rest = [ch for ch in s if ch != x and ch != y]
        xs = [ch for ch in s if ch == x]
        return "".join(ys + rest + xs)
