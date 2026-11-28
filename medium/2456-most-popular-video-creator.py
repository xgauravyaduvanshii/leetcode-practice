# LeetCode 2456. Most Popular Video Creator — Medium
# https://leetcode.com/problems/most-popular-video-creator/
# Submission 2204953152 — Accepted, Python3
#
# My thinking: add up the views per creator and remember each
# creator's best video — most views, ties broken by the smallest
# video id. Then return every creator whose total is the maximum,
# in the order they first appeared.
class Solution:
    def mostPopularCreator(self, creators: list[str], ids: list[str], views: list[int]) -> list[list[str]]:
        total = {}
        best = {}
        order = []
        for c, i, v in zip(creators, ids, views):
            if c not in total:
                total[c] = 0
                order.append(c)
            total[c] += v
            if c not in best or v > best[c][0] or (v == best[c][0] and i < best[c][1]):
                best[c] = (v, i)
        max_total = max(total.values())
        return [[c, best[c][1]] for c in order if total[c] == max_total]
