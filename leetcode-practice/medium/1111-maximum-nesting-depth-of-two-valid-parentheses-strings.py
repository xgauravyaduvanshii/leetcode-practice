# LeetCode 1111. Maximum Nesting Depth of Two Valid Parentheses Strings — Medium
# https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/
# Submission 2199001033 — Accepted, Python3
#
# My thinking: I hand each bracket to one of two
# groups by the depth it sits at — odd depths to
# one group, even depths to the other. Neither
# group ever gets deeper than half the original.

from typing import List


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        result = []
        depth = 0
        for ch in seq:
            if ch == "(":
                depth += 1
                result.append(depth % 2)
            else:
                result.append(depth % 2)
                depth -= 1
        return result
