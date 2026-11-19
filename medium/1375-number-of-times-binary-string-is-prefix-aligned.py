# LeetCode 1375. Number of Times Binary String Is Prefix-Aligned — Medium
# https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/
# Submission 2199043007 — Accepted, Python3
#
# My thinking: the flipped positions form a
# solid prefix exactly when the largest flipped
# position equals how many flips have happened.
# I track that largest position as I go.

from typing import List


class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = 0
        farthest = 0
        for i, value in enumerate(flips, 1):
            farthest = max(farthest, value)
            if farthest == i:
                count += 1
        return count
