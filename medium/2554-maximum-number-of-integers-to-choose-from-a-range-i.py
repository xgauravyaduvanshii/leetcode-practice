# LeetCode 2554. Maximum Number of Integers to Choose From a Range I — Medium
# https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/
# Submission 2205063944 — Accepted, Python3
#
# My thinking: to maximise the count under a sum cap, take the
# smallest allowed integers first — any solution can be swapped
# towards smaller numbers without breaking the cap. Walk 1..n,
# skip banned numbers, stop as soon as the next one would exceed
# maxSum.
class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
        total = count = 0
        for x in range(1, n + 1):
            if x in banned_set:
                continue
            if total + x > maxSum:
                break
            total += x
            count += 1
        return count
