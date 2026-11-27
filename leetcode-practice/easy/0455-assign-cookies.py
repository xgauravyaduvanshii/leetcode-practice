# LeetCode 455. Assign Cookies — Easy
# https://leetcode.com/problems/assign-cookies/
# Submission 2197478073 — Accepted, Python3
#
# My thinking: greedy. I sort both the children (by
# how greedy they are) and the cookies (by size),
# then walk through them together, always giving the
# smallest cookie that is big enough for the least
# greedy child still waiting.

class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        child = cookie = 0
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                child += 1
            cookie += 1
        return child
