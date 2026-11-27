# LeetCode 624. Maximum Distance in Arrays — Medium
# https://leetcode.com/problems/maximum-distance-in-arrays/
# Submission 2198887337 — Accepted, Python3
#
# My thinking: the two numbers must come from
# different arrays, so I keep the smallest first
# element and the largest last element seen so far
# and compare each new array against both of them.

from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        smallest = arrays[0][0]
        largest = arrays[0][-1]
        best = 0
        for arr in arrays[1:]:
            best = max(best, abs(arr[-1] - smallest), abs(largest - arr[0]))
            smallest = min(smallest, arr[0])
            largest = max(largest, arr[-1])
        return best
