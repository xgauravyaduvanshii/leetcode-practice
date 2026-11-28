# LeetCode 2610. Convert an Array Into a 2D Array With Conditions — Medium
# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/
# Submission 2205101336 — Accepted, Python3
#
# My thinking: each row must hold distinct values, so the
# number of rows is forced to be the highest frequency. Deal
# the elements out round by round — one copy of each remaining
# value per row — and every row comes out distinct with the
# minimum possible row count.
from collections import Counter


class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        freq = Counter(nums)
        ans = []
        while freq:
            row = []
            for x in list(freq):
                row.append(x)
                freq[x] -= 1
                if freq[x] == 0:
                    del freq[x]
            ans.append(row)
        return ans
