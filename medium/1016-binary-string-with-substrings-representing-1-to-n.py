# LeetCode 1016. Binary String With Substrings Representing 1 To N — Medium
# https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/
# Submission 2198986913 — Accepted, Python3
#
# My thinking: I just check every number from 1
# to n — its binary form must appear somewhere in
# the string. The first one that does not appear
# means the answer is no.

class Solution:
    def queryString(self, s: str, n: int) -> bool:
        for num in range(1, n + 1):
            if bin(num)[2:] not in s:
                return False
        return True
