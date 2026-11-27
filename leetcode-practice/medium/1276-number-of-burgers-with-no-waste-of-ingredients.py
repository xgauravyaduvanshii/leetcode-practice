# LeetCode 1276. Number of Burgers with No Waste of Ingredients — Medium
# https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/
# Submission 2199022388 — Accepted, Python3
#
# My thinking: a jumbo burger takes four tomato
# slices and one cheese, a small one two tomato
# and one cheese. Solving those two counts
# gives the jumbo number straight away, and the
# rest follows.

from typing import List


class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        jumbo = (tomatoSlices - 2 * cheeseSlices) // 2
        small = cheeseSlices - jumbo
        if tomatoSlices % 2 == 1 or jumbo < 0 or small < 0:
            return []
        return [jumbo, small]
