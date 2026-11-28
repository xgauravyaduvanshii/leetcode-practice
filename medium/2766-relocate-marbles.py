# LeetCode 2766. Relocate Marbles — Medium
# https://leetcode.com/problems/relocate-marbles/
# Submission 2205250253 — Accepted, Python3
#
# My thinking: only which positions are occupied matters, not
# how many marbles sit on each. Keep the occupied positions
# in a set; each move empties its source and fills its
# destination, then return the set sorted.
class Solution:
    def relocateMarbles(self, nums: list[int], moveFrom: list[int], moveTo: list[int]) -> list[int]:
        occupied = set(nums)
        for f, t in zip(moveFrom, moveTo):
            occupied.discard(f)
            occupied.add(t)
        return sorted(occupied)
