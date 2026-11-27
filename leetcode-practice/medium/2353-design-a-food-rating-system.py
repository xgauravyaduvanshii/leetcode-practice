# LeetCode 2353. Design a Food Rating System — Medium
# https://leetcode.com/problems/design-a-food-rating-system/
# Submission 2204733326 — Accepted, Python3
#
# My thinking: keep a food->(cuisine, rating) map, plus one max-heap per
# cuisine keyed by (-rating, food name) so the top is the highest-rated
# food, ties broken by the lexicographically smallest name. changeRating
# just pushes a fresh entry; highestRated lazily pops stale tops whose
# rating no longer matches the map.
import heapq

class FoodRatings:
    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.food_info = {}
        self.cuisine_heap = {}
        for f, c, r in zip(foods, cuisines, ratings):
            self.food_info[f] = (c, r)
            if c not in self.cuisine_heap:
                self.cuisine_heap[c] = []
            heapq.heappush(self.cuisine_heap[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        c, _ = self.food_info[food]
        self.food_info[food] = (c, newRating)
        heapq.heappush(self.cuisine_heap[c], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_heap[cuisine]
        while True:
            neg_r, food = heap[0]
            if self.food_info[food][1] == -neg_r:
                return food
            heapq.heappop(heap)
