# LeetCode 1395. Count Number of Teams — Medium
# https://leetcode.com/problems/count-number-of-teams/
# Submission 2199048430 — Accepted, Python3
#
# My thinking: for each middle soldier I count
# how many smaller and larger soldiers stand
# on each side. Smaller on the left times
# larger on the right, plus larger on the left
# times smaller on the right, is the number of
# teams with that middle.

from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        total = 0
        for j in range(n):
            left_smaller = left_larger = right_smaller = right_larger = 0
            for i in range(j):
                if rating[i] < rating[j]:
                    left_smaller += 1
                else:
                    left_larger += 1
            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    right_smaller += 1
                else:
                    right_larger += 1
            total += left_smaller * right_larger + left_larger * right_smaller
        return total
