# 3200. Maximum Height of a Triangle (Easy)
# https://leetcode.com/problems/maximum-height-of-a-triangle/
# Submission 2199984942 — Accepted, Python3
class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        # My thinking: try both ways round — red first,
        # then blue first. Each row takes one more ball
        # than the row before, alternating colours, and
        # the rows stop when the colour needed runs out.
        # The taller of the two tries wins.
        def height(first: int, second: int) -> int:
            rows = 0
            need = 1
            while True:
                if rows % 2 == 0:
                    if first < need:
                        return rows
                    first -= need
                else:
                    if second < need:
                        return rows
                    second -= need
                rows += 1
                need += 1

        return max(height(red, blue), height(blue, red))
