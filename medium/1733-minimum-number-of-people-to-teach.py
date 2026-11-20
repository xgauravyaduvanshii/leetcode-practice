# LeetCode 1733. Minimum Number of People to Teach — Medium
# https://leetcode.com/problems/minimum-number-of-people-to-teach/
# Submission 2199922310 — Accepted, Python3
#
# My thinking: only friendships where the two
# share no language matter. For each possible
# language I count how many of those people
# still need it, and I teach the cheapest one.

from typing import List


class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        knows = [set(langs) for langs in languages]
        needy = set()
        for a, b in friendships:
            a -= 1
            b -= 1
            if not (knows[a] & knows[b]):
                needy.add(a)
                needy.add(b)
        if not needy:
            return 0
        best = len(needy)
        for lang in range(1, n + 1):
            teach = sum(1 for person in needy if lang not in knows[person])
            best = min(best, teach)
        return best
