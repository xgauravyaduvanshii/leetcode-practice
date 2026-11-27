# LeetCode 28. Find the Index of the First Occurrence in a String — Easy
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Submission 2197280350 — Accepted, Python3
#
# My thinking: I just need the first place where the
# needle appears inside the haystack. Python's find
# does exactly that and returns -1 when it is not there.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
