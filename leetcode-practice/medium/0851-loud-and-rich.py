# LeetCode 851. Loud and Rich — Medium
# https://leetcode.com/problems/loud-and-rich/
# Submission 2198955608 — Accepted, Python3
#
# My thinking: richer people pass their quietness
# down to everyone poorer than them. I walk each
# person's richer chain with memoisation and keep
# the quietest person I find.

from typing import List


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = [[] for _ in range(n)]
        for a, b in richer:
            graph[b].append(a)
        answer = [-1] * n

        def quietest(person):
            if answer[person] != -1:
                return answer[person]
            best = person
            for richer_person in graph[person]:
                candidate = quietest(richer_person)
                if quiet[candidate] < quiet[best]:
                    best = candidate
            answer[person] = best
            return best

        return [quietest(person) for person in range(n)]
