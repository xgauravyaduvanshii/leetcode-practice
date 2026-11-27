# LeetCode 2102. Sequentially Ordinal Rank Tracker — Hard
# https://leetcode.com/problems/sequentially-ordinal-rank-tracker/
# Submission 2201572673 — Accepted, Python3
#
# My thinking: the next get asks for the next
# best place, so I keep the best few in one
# heap and the rest in another — each add drops
# into the rest and swaps up if it beats the
# worst of the best, and each get pulls the
# best of the rest into the best.

import heapq


class _Item:
    # Heap order: the worst item comes first (lowest score, then largest name).
    __slots__ = ("score", "name")

    def __init__(self, score, name):
        self.score = score
        self.name = name

    def __lt__(self, other):
        if self.score != other.score:
            return self.score < other.score
        return self.name > other.name


class SORTracker:
    def __init__(self):
        self.top = []   # min-heap of _Item, worst of the top k on top
        self.rest = []  # min-heap of (-score, name), best of the rest on top
        self.k = 0

    def add(self, name: str, score: int) -> None:
        heapq.heappush(self.rest, (-score, name))
        if self.top:
            worst = self.top[0]
            best_score, best_name = -self.rest[0][0], self.rest[0][1]
            if best_score > worst.score or (best_score == worst.score and best_name < worst.name):
                heapq.heappop(self.rest)
                heapq.heappop(self.top)
                heapq.heappush(self.top, _Item(best_score, best_name))
                heapq.heappush(self.rest, (-worst.score, worst.name))

    def get(self) -> str:
        self.k += 1
        score, name = heapq.heappop(self.rest)
        heapq.heappush(self.top, _Item(-score, name))
        return self.top[0].name
