# LeetCode 575. Distribute Candies — Easy
# https://leetcode.com/problems/distribute-candies/
# Submission 2197501216 — Accepted, Python3
#
# My thinking: I can eat at most half the candies,
# and I cannot eat more different kinds than exist.
# So the answer is whichever of those two numbers
# is smaller.

class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        return min(len(set(candyType)), len(candyType) // 2)
