# LeetCode 1961. Check If String Is a Prefix of Array — Easy
# https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/
# Submission 2197606206 — Accepted, Python3
#
# My thinking: I build the string word by word. As
# soon as the built string equals s, it is a prefix.
# If the built string grows longer than s, it can
# never match. If I run out of words without a
# match, the answer is false.

class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
        built = ""
        for w in words:
            built += w
            if built == s:
                return True
            if len(built) > len(s):
                return False
        return False
