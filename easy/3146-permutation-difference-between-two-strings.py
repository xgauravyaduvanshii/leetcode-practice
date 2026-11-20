# 3146. Permutation Difference Between Two Strings (Easy)
# https://leetcode.com/problems/permutation-difference-between-two-strings/
# Submission 2199979714 — Accepted, Python3
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        # My thinking: for each letter, note where it
        # sits in each string. The difference is the
        # total of how far every letter moved.
        pos = {ch: i for i, ch in enumerate(t)}
        return sum(abs(i - pos[ch]) for i, ch in enumerate(s))
