# LeetCode 3019. Number of Changing Keys — Easy
# https://leetcode.com/problems/number-of-changing-keys/
# Submission 2198715917 — Accepted, Python3
#
# My thinking: only the letter matters, not whether
# it is upper or lower case. I walk the string and
# count each time the letter changes from the one
# before it.

class Solution:
    def countKeyChanges(self, s: str) -> int:
        changes = 0
        for i in range(1, len(s)):
            if s[i].lower() != s[i - 1].lower():
                changes += 1
        return changes
