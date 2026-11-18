# LeetCode 911. Online Election — Medium
# https://leetcode.com/problems/online-election/
# Submission 2198968436 — Accepted, Python3
#
# My thinking: I replay the votes once, keeping
# the leader after every vote. A query is then
# just a binary search for the latest vote at or
# before the given time.

import bisect
from typing import List


class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        votes = {}
        leader = -1
        self.leaders = []
        for person in persons:
            votes[person] = votes.get(person, 0) + 1
            if votes[person] >= votes.get(leader, 0):
                leader = person
            self.leaders.append(leader)

    def q(self, t: int) -> int:
        index = bisect.bisect_right(self.times, t) - 1
        return self.leaders[index]
