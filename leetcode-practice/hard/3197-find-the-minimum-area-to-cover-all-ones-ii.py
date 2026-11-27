# LeetCode 3197. Find the Minimum Area to Cover All Ones II — Hard
# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/
# Submission 2202075637 — Accepted, Python3
#
# My thinking: three rectangles covering
# all ones must come from one of a few
# cut shapes: three vertical strips,
# three horizontal strips, or an L-cut
# in one of four orientations. For any
# rectangle I find its tight bounding box
# with a 2D prefix sum, and try every cut
# position in every shape.

from typing import List


class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ps = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            row = 0
            for j in range(n):
                row += grid[i][j]
                ps[i + 1][j + 1] = ps[i][j + 1] + row

        def rect_sum(top, bottom, left, right):
            return ps[bottom][right] - ps[top][right] - ps[bottom][left] + ps[top][left]

        def area(top, bottom, left, right):
            if rect_sum(top, bottom, left, right) == 0:
                return 0
            minr = top
            while rect_sum(minr, minr + 1, left, right) == 0:
                minr += 1
            maxr = bottom - 1
            while rect_sum(maxr, maxr + 1, left, right) == 0:
                maxr -= 1
            minc = left
            while rect_sum(top, bottom, minc, minc + 1) == 0:
                minc += 1
            maxc = right - 1
            while rect_sum(top, bottom, maxc, maxc + 1) == 0:
                maxc -= 1
            return (maxr - minr + 1) * (maxc - minc + 1)

        ans = 10 ** 9
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                ans = min(ans, area(0, m, 0, i) + area(0, m, i, j) + area(0, m, j, n))
        for i in range(1, m - 1):
            for j in range(i + 1, m):
                ans = min(ans, area(0, i, 0, n) + area(i, j, 0, n) + area(j, m, 0, n))
        for c in range(1, n):
            for r in range(1, m):
                ans = min(ans, area(0, r, 0, c) + area(r, m, 0, c) + area(0, m, c, n))
                ans = min(ans, area(0, m, 0, c) + area(0, r, c, n) + area(r, m, c, n))
        for r in range(1, m):
            for c in range(1, n):
                ans = min(ans, area(0, r, 0, c) + area(0, r, c, n) + area(r, m, 0, n))
                ans = min(ans, area(0, r, 0, n) + area(r, m, 0, c) + area(r, m, c, n))
        return ans
