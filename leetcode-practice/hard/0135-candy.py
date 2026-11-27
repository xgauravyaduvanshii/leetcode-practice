# LeetCode 135. Candy — Hard
# https://leetcode.com/problems/candy/
# Submission 2198388608 — Accepted, Python3
#
# My thinking: every child starts with one candy.
# I walk left to right giving one more candy than
# the left neighbour whenever the rating rises.
# Then I walk right to left doing the same against
# the right neighbour, keeping the bigger of the
# two counts so both sides stay happy. The total
# is the smallest number of candies that works.

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        return sum(candies)
