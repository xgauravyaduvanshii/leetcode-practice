# LeetCode 386. Lexicographical Numbers — Medium
# https://leetcode.com/problems/lexicographical-numbers/
# Submission 2198767752 — Accepted, Python3
#
# My thinking: lexicographic order is a pre-order
# walk of a tree where each number's children are
# itself times ten. I walk it without building the
# tree — go deeper while the next child fits, else
# step to the next sibling, climbing up past
# trailing nines.

from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        current = 1
        for _ in range(n):
            result.append(current)
            if current * 10 <= n:
                current *= 10
            else:
                if current >= n:
                    current //= 10
                current += 1
                while current % 10 == 0:
                    current //= 10
        return result
