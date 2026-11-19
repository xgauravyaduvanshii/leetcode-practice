# LeetCode 1104. Path In Zigzag Labelled Binary Tree — Medium
# https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/
# Submission 2199000288 — Accepted, Python3
#
# My thinking: I walk from the label up to the
# root. On each level the labels run backwards,
# so I mirror the label within its level and
# take the parent in a normal tree.

from typing import List


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        path = []
        while label >= 1:
            path.append(label)
            level = label.bit_length()
            label = ((1 << level) + (1 << (level - 1)) - 1 - label) // 2
        return path[::-1]
