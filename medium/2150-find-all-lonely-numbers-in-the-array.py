# LeetCode 2150. Find All Lonely Numbers in the Array — Medium
# https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/
# Submission 2204475802 — Accepted, Python3
#
# My thinking: a number is lonely when it appears exactly once and
# neither neighbour (x - 1 or x + 1) appears at all. I count frequencies
# and keep the values in a set, then keep only the numbers that pass
# both checks.
class Solution:
    def findLonely(self, nums: list[int]) -> list[int]:
        from collections import Counter
        cnt = Counter(nums)
        s = set(nums)
        return [x for x, c in cnt.items() if c == 1 and (x - 1) not in s and (x + 1) not in s]
