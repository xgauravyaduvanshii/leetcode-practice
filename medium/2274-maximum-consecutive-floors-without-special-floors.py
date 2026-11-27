# LeetCode 2274. Maximum Consecutive Floors Without Special Floors — Medium
# https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/
# Submission 2204619581 — Accepted, Python3
#
# My thinking: sort the special floors. The free stretches are: from
# the bottom up to the first special floor, between each pair of
# neighbouring special floors, and from the last special floor up to the
# top. The answer is simply the longest of those stretches.
class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: list[int]) -> int:
        special.sort()
        return max([special[0] - bottom, top - special[-1]] + [special[i] - special[i - 1] - 1 for i in range(1, len(special))])
