# LeetCode 2739. Total Distance Traveled — Easy
# https://leetcode.com/problems/total-distance-traveled/
# Submission 2198357735 — Accepted, Python3
#
# My thinking: the car goes 10 km on every litre.
# I keep using the main tank five litres at a time,
# and each time I move one litre over from the
# extra tank if there is any left. Whatever stays
# in the main tank at the end is worth 10 km a litre.

class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        distance = 0
        while mainTank >= 5:
            distance += 50
            mainTank -= 5
            if additionalTank > 0:
                additionalTank -= 1
                mainTank += 1
        distance += mainTank * 10
        return distance
