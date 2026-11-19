# LeetCode 1333. Filter Restaurants by Vegan-Friendly, Price and Distance — Medium
# https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/
# Submission 2199032914 — Accepted, Python3
#
# My thinking: I keep only the restaurants
# that pass every filter, then order them by
# rating, and by id when the ratings tie.

from typing import List


class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        kept = [r for r in restaurants if (not veganFriendly or r[2] == 1) and r[3] <= maxPrice and r[4] <= maxDistance]
        kept.sort(key=lambda r: (-r[1], -r[0]))
        return [r[0] for r in kept]
