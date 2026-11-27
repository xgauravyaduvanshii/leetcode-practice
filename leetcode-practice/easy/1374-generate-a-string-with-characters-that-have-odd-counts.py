# LeetCode 1374. Generate a String With Characters That Have Odd Counts — Easy
# https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/
# Submission 2197574490 — Accepted, Python3
#
# My thinking: if n is odd, all a's works — a appears
# n times, which is odd. If n is even, I use n-1
# a's (odd) plus one b (odd). That is the whole trick.

class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 1:
            return "a" * n
        return "a" * (n - 1) + "b"
