"""LeetCode 14. Longest Common Prefix — Easy
https://leetcode.com/problems/longest-common-prefix/
Submission 2197268260 — Accepted, 126/126 testcases, Python3
"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
