# LeetCode 969. Pancake Sorting — Medium
# https://leetcode.com/problems/pancake-sorting/
# Submission 2198979106 — Accepted, Python3
#
# My thinking: I place the biggest pancake first
# — flip it to the top, then flip the whole
# stack so it lands at the bottom. Then I do the
# same for the next biggest, one at a time.

from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        size = len(arr)
        for target in range(size, 1, -1):
            index = arr.index(target)
            if index == target - 1:
                continue
            if index != 0:
                flips.append(index + 1)
                arr[:index + 1] = reversed(arr[:index + 1])
            flips.append(target)
            arr[:target] = reversed(arr[:target])
        return flips
