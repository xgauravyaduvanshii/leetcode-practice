# LeetCode 1238. Circular Permutation in Binary Representation — Medium
# https://leetcode.com/problems/circular-permutation-in-binary-representation/
# Submission 2199017177 — Accepted, Python3
#
# My thinking: the Gray code lists every number
# with neighbours one bit apart. I build that
# list, then rotate it so it starts at the
# given number.

from typing import List


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        gray = [i ^ (i >> 1) for i in range(1 << n)]
        index = gray.index(start)
        return gray[index:] + gray[:index]
