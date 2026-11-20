# LeetCode 1583. Count Unhappy Friends — Medium
# https://leetcode.com/problems/count-unhappy-friends/
# Submission 2199884597 — Accepted, Python3
#
# My thinking: a friend is unhappy when
# someone they prefer over their partner also
# prefers them over their own partner. I rank
# every preference list once, then check each
# friend against the people ahead of their
# partner.

from typing import List


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        rank = [[0] * n for _ in range(n)]
        for person in range(n):
            for pos, other in enumerate(preferences[person]):
                rank[person][other] = pos
        partner = [0] * n
        for a, b in pairs:
            partner[a] = b
            partner[b] = a
        unhappy = 0
        for x in range(n):
            y = partner[x]
            for u in preferences[x]:
                if u == y:
                    break
                v = partner[u]
                if rank[u][x] < rank[u][v]:
                    unhappy += 1
                    break
        return unhappy
