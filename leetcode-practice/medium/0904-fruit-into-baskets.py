# LeetCode 904. Fruit Into Baskets — Medium
# https://leetcode.com/problems/fruit-into-baskets/
# Submission 2198966113 — Accepted, Python3
#
# My thinking: I grow a window from the left and
# keep the count of each fruit type inside it.
# The moment a third type appears, I shrink the
# window from the left until only two remain.

from collections import defaultdict
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counts = defaultdict(int)
        best = 0
        left = 0
        for right, fruit in enumerate(fruits):
            counts[fruit] += 1
            while len(counts) > 2:
                counts[fruits[left]] -= 1
                if counts[fruits[left]] == 0:
                    del counts[fruits[left]]
                left += 1
            best = max(best, right - left + 1)
        return best
