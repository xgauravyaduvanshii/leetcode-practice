# LeetCode 649. Dota2 Senate — Medium
# https://leetcode.com/problems/dota2-senate/
# Submission 2198897557 — Accepted, Python3
#
# My thinking: each senator bans the next enemy
# senator in line, then rejoins the queue for the
# next round. The side whose senators run out
# first loses.

from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque(i for i, s in enumerate(senate) if s == "R")
        dire = deque(i for i, s in enumerate(senate) if s == "D")
        n = len(senate)
        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()
            if r < d:
                radiant.append(r + n)
            else:
                dire.append(d + n)
        return "Radiant" if radiant else "Dire"
