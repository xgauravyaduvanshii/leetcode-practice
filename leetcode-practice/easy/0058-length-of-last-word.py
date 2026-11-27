# LeetCode 58. Length of Last Word — Easy
# https://leetcode.com/problems/length-of-last-word/
# Submission 2197281048 — Accepted, Python3
#
# My thinking: split the string on whitespace and the
# last piece is the last word — its length is the answer.
# Splitting also takes care of any trailing spaces.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
