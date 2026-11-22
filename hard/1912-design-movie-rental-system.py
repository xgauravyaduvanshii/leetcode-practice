# LeetCode 1912. Design Movie Rental System — Hard
# https://leetcode.com/problems/design-movie-rental-system/
# Submission 2201229599 — Accepted, Python3
#
# My thinking: unrented copies sit in a heap per
# movie ordered by price then shop, rented copies
# in one heap ordered by price then shop then
# movie — a rented set tells me which heap entries
# have gone stale, so I skip them lazily.

import heapq

class MovieRentingSystem:
    def __init__(self, n: int, entries: list[list[int]]):
        self.prices = {}
        self.unrented = {}
        self.rented = []
        self.rented_set = set()
        for shop, movie, price in entries:
            self.prices[(shop, movie)] = price
            self.unrented.setdefault(movie, []).append((price, shop))
        for movie in self.unrented:
            heapq.heapify(self.unrented[movie])

    def search(self, movie: int) -> list[int]:
        heap = self.unrented.get(movie, [])
        res = []
        tmp = []
        while heap and len(res) < 5:
            price, shop = heapq.heappop(heap)
            if (shop, movie) not in self.rented_set:
                res.append(shop)
            tmp.append((price, shop))
        for item in tmp:
            heapq.heappush(heap, item)
        return res

    def rent(self, shop: int, movie: int) -> None:
        self.rented_set.add((shop, movie))
        heapq.heappush(self.rented, (self.prices[(shop, movie)], shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        self.rented_set.discard((shop, movie))

    def report(self) -> list[list[int]]:
        res = []
        tmp = []
        seen = set()
        while self.rented and len(res) < 5:
            price, shop, movie = heapq.heappop(self.rented)
            if (shop, movie) not in self.rented_set or (shop, movie) in seen:
                continue
            seen.add((shop, movie))
            res.append([shop, movie])
            tmp.append((price, shop, movie))
        for item in tmp:
            heapq.heappush(self.rented, item)
        return res
