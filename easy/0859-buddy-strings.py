# LeetCode 859. Buddy Strings — Easy
# https://leetcode.com/problems/buddy-strings/
# Submission 2197535521 — Accepted, Python3
#
# My thinking: swapping two letters can only fix
# exactly two mismatched positions, and the two
# letters have to be crossed over. If the strings
# are already equal, a swap is only possible when
# some letter repeats (swap those two and nothing
# changes). Different lengths can never work.

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return len(set(s)) < len(s)
        diffs = [(a, b) for a, b in zip(s, goal) if a != b]
        return len(diffs) == 2 and diffs[0] == diffs[1][::-1]
