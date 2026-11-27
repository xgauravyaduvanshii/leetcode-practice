# LeetCode 1541. Minimum Insertions to Balance a Parentheses String — Medium
# https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/
# Submission 2199871833 — Accepted, Python3
#
# My thinking: I read the string left to
# right. A lone "(" needs two ")" after it;
# a ")" with no open "(" before it needs one
# inserted. Leftover opens each need two
# closes at the end.

class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        open_needed = 0
        i = 0
        while i < len(s):
            if s[i] == "(":
                open_needed += 1
                i += 1
            else:
                if open_needed > 0:
                    open_needed -= 1
                else:
                    insertions += 1
                if i + 1 < len(s) and s[i + 1] == ")":
                    i += 2
                else:
                    insertions += 1
                    i += 1
        return insertions + open_needed * 2
