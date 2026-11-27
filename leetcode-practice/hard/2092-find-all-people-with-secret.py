# LeetCode 2092. Find All People With Secret — Hard
# https://leetcode.com/problems/find-all-people-with-secret/
# Submission 2201569080 — Accepted, Python3
#
# My thinking: meetings that share a time can
# pass the secret around among themselves, so I
# take each time-slice on its own, link everyone
# meeting then, and spread the secret from
# whoever already knows it before that slice.

from collections import defaultdict, deque


class Solution:
    def findAllPeople(self, n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
        know = {0, firstPerson}
        meetings.sort(key=lambda m: m[2])
        i = 0
        while i < len(meetings):
            j = i
            while j < len(meetings) and meetings[j][2] == meetings[i][2]:
                j += 1
            graph = defaultdict(list)
            people = set()
            for a, b, _ in meetings[i:j]:
                graph[a].append(b)
                graph[b].append(a)
                people.add(a)
                people.add(b)
            q = deque(p for p in people if p in know)
            seen = set(q)
            while q:
                u = q.popleft()
                know.add(u)
                for v in graph[u]:
                    if v not in seen:
                        seen.add(v)
                        q.append(v)
            i = j
        return sorted(know)
