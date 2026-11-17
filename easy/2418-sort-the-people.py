# LeetCode 2418. Sort the People — Easy
# https://leetcode.com/problems/sort-the-people/
# Submission 2197781378 — Accepted, Python3
#
# My thinking: I pair each name with its height and
# sort the pairs by height from tallest to shortest,
# then read off the names in that order.

class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        return [name for _, name in sorted(zip(heights, names), reverse=True)]
