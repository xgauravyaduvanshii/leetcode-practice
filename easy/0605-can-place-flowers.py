# LeetCode 605. Can Place Flowers — Easy
# https://leetcode.com/problems/can-place-flowers/
# Submission 2197504510 — Accepted, Python3
#
# My thinking: greedy — I walk along the bed and
# plant a flower wherever the spot and both its
# neighbours are empty. Planting early never hurts,
# because a flower only blocks its own neighbours.
# I count how many I planted and check if it is
# enough.

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)
        for i in range(length):
            if flowerbed[i] == 0:
                empty_left = i == 0 or flowerbed[i - 1] == 0
                empty_right = i == length - 1 or flowerbed[i + 1] == 0
                if empty_left and empty_right:
                    flowerbed[i] = 1
                    count += 1
        return count >= n
