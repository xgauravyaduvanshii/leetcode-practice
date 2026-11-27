# LeetCode 2225. Find Players With Zero or One Losses — Medium
# https://leetcode.com/problems/find-players-with-zero-or-one-losses/
# Submission 2204509159 — Accepted, Python3
#
# My thinking: I count each player's losses and remember everyone who
# won at least one match. Players who won but never lost are the zero-
# loss list, and players whose loss count is exactly one are the one-
# loss list; both lists come out sorted.
class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        from collections import Counter
        losses = Counter()
        winners = set()
        for w, l in matches:
            winners.add(w)
            losses[l] += 1
        zero = sorted(p for p in winners if losses[p] == 0)
        one = sorted(p for p, c in losses.items() if c == 1)
        return [zero, one]
