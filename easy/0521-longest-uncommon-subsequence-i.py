# LeetCode 521. Longest Uncommon Subsequence I — Easy
# https://leetcode.com/problems/longest-uncommon-subsequence-i/
# Submission 2197493630 — Accepted, Python3
#
# My thinking: if the two strings are the same, there
# is no uncommon subsequence at all. Otherwise the
# longer string itself is a subsequence that the
# other one does not have — so its length is the
# answer.

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        return max(len(a), len(b))
