# LeetCode 1366. Rank Teams by Votes — Medium
# https://leetcode.com/problems/rank-teams-by-votes/
# Submission 2199041549 — Accepted, Python3
#
# My thinking: each team's score is its count
# of first places, then second places, and so
# on. Sorting by those counts, with the team
# name breaking ties, gives the ranking.

from collections import defaultdict
from typing import List


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        scores = defaultdict(lambda: [0] * len(votes[0]))
        for vote in votes:
            for i, team in enumerate(vote):
                scores[team][i] -= 1
        return "".join(sorted(scores, key=lambda team: (scores[team], team)))
