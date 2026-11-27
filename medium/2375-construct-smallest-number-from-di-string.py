# LeetCode 2375. Construct Smallest Number From DI String — Medium
# https://leetcode.com/problems/construct-smallest-number-from-di-string/
# Submission 2204765987 — Accepted, Python3
#
# My thinking: walk the pattern pushing the digits 1..n+1 onto a stack.
# Every 'I' (and the end) flushes the stack: the digits come out
# reversed, which is exactly what a run of 'D's needs, and flushing at
# each 'I' keeps the result as small as possible.
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = []
        stack = []
        n = len(pattern)
        for i in range(n + 1):
            stack.append(str(i + 1))
            if i == n or pattern[i] == 'I':
                while stack:
                    res.append(stack.pop())
        return ''.join(res)
