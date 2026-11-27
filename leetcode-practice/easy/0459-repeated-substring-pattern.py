# LeetCode 459. Repeated Substring Pattern — Easy
# https://leetcode.com/problems/repeated-substring-pattern/
# Submission 2197479034 — Accepted, Python3
#
# My thinking: if a string is made of a smaller piece
# repeated, then writing it twice and cutting off
# the first and last characters will still contain
# the original string inside. If it is not made of
# repeats, it will not.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]
