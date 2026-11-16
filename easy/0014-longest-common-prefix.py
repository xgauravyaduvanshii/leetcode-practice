# LeetCode 14. Longest Common Prefix — Easy
# https://leetcode.com/problems/longest-common-prefix/
# Submission 2197268260 — Accepted, Python3
#
# My thinking: start by assuming the whole first word is
# the prefix. Then check it against every other word —
# if a word does not start with it, chop one letter off
# the end and try again. If nothing is left, there is
# no common prefix at all.

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix
