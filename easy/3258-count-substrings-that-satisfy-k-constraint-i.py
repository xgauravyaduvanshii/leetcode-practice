# 3258. Count Substrings That Satisfy K-Constraint I (Easy)
# https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/
# Submission 2199990501 — Accepted, Python3
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        # My thinking: a substring counts when it holds
        # at most k zeroes or at most k ones — either one
        # is enough. I grow each substring from every
        # starting spot and stop only when both counts
        # have passed k, since longer ones can only get
        # worse from there.
        n = len(s)
        count = 0
        for start in range(n):
            zeros = 0
            ones = 0
            for end in range(start, n):
                if s[end] == "0":
                    zeros += 1
                else:
                    ones += 1
                if zeros > k and ones > k:
                    break
                count += 1
        return count
