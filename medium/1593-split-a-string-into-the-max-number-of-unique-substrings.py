# LeetCode 1593. Split a String Into the Max Number of Unique Substrings — Medium
# https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/
# Submission 2199886455 — Accepted, Python3
#
# My thinking: I try every split by
# backtracking, keeping only pieces I have
# not used before. Short pieces first keeps
# the count high, and I prune any branch that
# cannot beat the best so far.

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        best = [0]

        def backtrack(index, seen):
            if index == len(s):
                best[0] = max(best[0], len(seen))
                return
            if len(seen) + (len(s) - index) <= best[0]:
                return
            for end in range(index + 1, len(s) + 1):
                piece = s[index:end]
                if piece not in seen:
                    seen.add(piece)
                    backtrack(end, seen)
                    seen.remove(piece)

        backtrack(0, set())
        return best[0]
