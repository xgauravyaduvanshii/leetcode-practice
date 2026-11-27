# LeetCode 1854. Maximum Population Year — Easy
# https://leetcode.com/problems/maximum-population-year/
# Submission 2197601525 — Accepted, Python3
#
# My thinking: for each person I count every year
# from their birth year up to (but not including)
# their death year. The year with the biggest count
# is the answer; ties go to the earliest year.

class Solution:
    def maximumPopulation(self, logs: list[list[int]]) -> int:
        pop = {}
        for birth, death in logs:
            for y in range(birth, death):
                pop[y] = pop.get(y, 0) + 1
        return max(pop, key=lambda y: (pop[y], -y))
