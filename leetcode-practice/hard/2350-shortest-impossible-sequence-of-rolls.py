# LeetCode 2350. Shortest Impossible Sequence of Rolls — Hard
# https://leetcode.com/problems/shortest-impossible-sequence-of-rolls/
# Submission 2201694486 — Accepted, Python3
#
# My thinking: a sequence only survives
# while every face keeps showing up — I
# count how many full rounds of all faces
# the rolls hold, and the shortest one
# they lack is one longer than that.

class Solution:
    def shortestSequence(self, rolls: list[int], k: int) -> int:
        rounds = 0
        seen = set()
        for r in rolls:
            seen.add(r)
            if len(seen) == k:
                rounds += 1
                seen = set()
        return rounds + 1
