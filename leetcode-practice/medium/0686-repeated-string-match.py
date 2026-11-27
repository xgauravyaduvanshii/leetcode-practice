# LeetCode 686. Repeated String Match — Medium
# https://leetcode.com/problems/repeated-string-match/
# Submission 2197514789 — Accepted, Python3
#
# My thinking: I keep repeating a until it is at
# least as long as b. If b is inside it now, that
# count is the answer. If not, one more copy might
# do it — b could start near the end of the last
# copy. If it is still not there, it never will be.

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeated = a
        count = 1
        while len(repeated) < len(b):
            repeated += a
            count += 1
        if b in repeated:
            return count
        if b in repeated + a:
            return count + 1
        return -1
