# LeetCode 2191. Sort the Jumbled Numbers — Medium
# https://leetcode.com/problems/sort-the-jumbled-numbers/
# Submission 2204494636 — Accepted, Python3
#
# My thinking: each number's mapped value is found by replacing every
# digit through the mapping, so I sort the original numbers by that
# mapped value. Python's sort is stable, so numbers with equal mapped
# values keep their original relative order, exactly as required.
class Solution:
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        def mapped(x):
            return int(''.join(str(mapping[int(d)]) for d in str(x)))
        return sorted(nums, key=mapped)
