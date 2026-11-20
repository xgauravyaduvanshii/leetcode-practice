# LeetCode 1744. Can You Eat Your Favorite Candy on Your Favorite Day? — Medium
# https://leetcode.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/
# Submission 2199926649 — Accepted, Python3
#
# My thinking: by the favourite day I have
# eaten at most a day's cap times the days,
# and at least one candy a day. The favourite
# type is reachable when those bounds overlap
# its range in the pile.

from typing import List


class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        prefix = [0]
        for count in candiesCount:
            prefix.append(prefix[-1] + count)
        result = []
        for favoriteType, favoriteDay, dailyCap in queries:
            most = (favoriteDay + 1) * dailyCap
            result.append(prefix[favoriteType] < most and prefix[favoriteType + 1] > favoriteDay)
        return result
