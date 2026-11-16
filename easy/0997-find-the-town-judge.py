# LeetCode 997. Find the Town Judge — Easy
# https://leetcode.com/problems/find-the-town-judge/
# Submission 2197549692 — Accepted, Python3
#
# My thinking: the judge is trusted by everyone
# else and trusts nobody. So I count, for each
# person, how many people trust them and how many
# they trust. The judge is the one trusted by all
# n - 1 others with zero outgoing trust. With one
# person, they are the judge by default.

class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if n == 1:
            return 1
        indegree = [0] * (n + 1)
        outdegree = [0] * (n + 1)
        for a, b in trust:
            outdegree[a] += 1
            indegree[b] += 1
        for i in range(1, n + 1):
            if indegree[i] == n - 1 and outdegree[i] == 0:
                return i
        return -1
