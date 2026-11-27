# 3931. Check Adjacent Digit Differences (Easy)
# https://leetcode.com/problems/check-adjacent-digit-differences/
# Submission 2200088581 — Accepted, Python3
class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        # My thinking: I walk the digits and check
        # each neighbouring pair — if any two differ
        # by more than two, the answer is no.
        return all(abs(int(s[i]) - int(s[i + 1])) <= 2 for i in range(len(s) - 1))
