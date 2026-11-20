# 3238. Find the Number of Winning Players (Easy)
# https://leetcode.com/problems/find-the-number-of-winning-players/
# Submission 2199989448 — Accepted, Python3
from collections import Counter, defaultdict
from typing import List


class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        # My thinking: for each player, count how many
        # balls of each colour they picked. A player wins
        # when some colour's count beats their own number
        # — player 0 needs more than 0, player 1 more
        # than 1, and so on.
        picks = defaultdict(Counter)
        for player, color in pick:
            picks[player][color] += 1
        winners = 0
        for player in range(n):
            if any(count > player for count in picks[player].values()):
                winners += 1
        return winners
