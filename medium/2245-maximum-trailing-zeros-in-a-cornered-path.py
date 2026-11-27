# LeetCode 2245. Maximum Trailing Zeros in a Cornered Path — Medium
# https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/
# Submission 2204515784 — Accepted, Python3
#
# My thinking: trailing zeros of a product come from min(count of 2s,
# count of 5s), so I count both factors for every cell and build row and
# column prefix sums. A cornered path through a cell is one vertical arm
# plus one horizontal arm, and the cell itself must be counted once, not
# twice. I try all four arm combinations at every cell and keep the best
# min(2s, 5s).
class Solution:
    def maxTrailingZeros(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def count_factors(x, p):
            c = 0
            while x % p == 0:
                x //= p
                c += 1
            return c

        two = [[0] * n for _ in range(m)]
        five = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                two[i][j] = count_factors(grid[i][j], 2)
                five[i][j] = count_factors(grid[i][j], 5)

        row2 = [[0] * (n + 1) for _ in range(m)]
        row5 = [[0] * (n + 1) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                row2[i][j + 1] = row2[i][j] + two[i][j]
                row5[i][j + 1] = row5[i][j] + five[i][j]

        col2 = [[0] * n for _ in range(m + 1)]
        col5 = [[0] * n for _ in range(m + 1)]
        for j in range(n):
            for i in range(m):
                col2[i + 1][j] = col2[i][j] + two[i][j]
                col5[i + 1][j] = col5[i][j] + five[i][j]

        ans = 0
        for i in range(m):
            for j in range(n):
                up2 = col2[i + 1][j]
                up5 = col5[i + 1][j]
                down2 = col2[m][j] - col2[i][j]
                down5 = col5[m][j] - col5[i][j]
                left2 = row2[i][j + 1]
                left5 = row5[i][j + 1]
                right2 = row2[i][n] - row2[i][j]
                right5 = row5[i][n] - row5[i][j]
                t2 = two[i][j]
                t5 = five[i][j]
                for v2, v5, h2, h5 in ((up2, up5, left2, left5), (up2, up5, right2, right5), (down2, down5, left2, left5), (down2, down5, right2, right5)):
                    s2 = v2 + h2 - t2
                    s5 = v5 + h5 - t5
                    if min(s2, s5) > ans:
                        ans = min(s2, s5)
        return ans
