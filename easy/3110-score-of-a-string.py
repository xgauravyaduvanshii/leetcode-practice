# 3110. Score of a String (Easy)
# https://leetcode.com/problems/score-of-a-string/
# Submission 2199977853 — Accepted, Python3
class Solution:
    def scoreOfString(self, s: str) -> int:
        # My thinking: the score is just how much each
        # letter jumps from its neighbour, added up.
        # Neighbouring letters are compared by their
        # alphabet positions, and every jump counts.
        total = 0
        for i in range(len(s) - 1):
            total += abs(ord(s[i]) - ord(s[i + 1]))
        return total
