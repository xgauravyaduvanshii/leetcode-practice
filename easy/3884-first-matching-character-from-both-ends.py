# 3884. First Matching Character From Both Ends (Easy)
# https://leetcode.com/problems/first-matching-character-from-both-ends/
# Submission 2200084379 — Accepted, Python3
class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        # My thinking: I check each position against
        # its mirror image from the other end, starting
        # from the left — the first match is the
        # answer.
        n = len(s)
        for i in range(n):
            if s[i] == s[n - 1 - i]:
                return i
        return -1
