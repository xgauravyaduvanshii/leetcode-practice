# 4043. Count Rotations With Exactly K Equal Adjacent Pairs (Easy)
# https://leetcode.com/problems/count-rotations-with-exactly-k-equal-adjacent-pairs/
# Submission 2200099505 — Accepted, Python3
class Solution:
    def countRotations(self, s: str, k: int) -> int:
        # My thinking: I try every rotation of the
        # string and count the neighbouring pairs that
        # match — the answer is how many rotations
        # have exactly k such pairs.
        n = len(s)
        ans = 0
        for r in range(n):
            rot = s[r:] + s[:r]
            score = sum(1 for i in range(n - 1) if rot[i] == rot[i + 1])
            if score == k:
                ans += 1
        return ans
