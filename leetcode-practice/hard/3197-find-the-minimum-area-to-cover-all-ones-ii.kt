// LeetCode 3197. Find the Minimum Area to Cover All Ones II — Hard
// https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-ii/
// Submission 2202076662 — Accepted, Kotlin
//
// My thinking: three rectangles covering
// all ones must come from one of a few
// cut shapes: three vertical strips,
// three horizontal strips, or an L-cut
// in one of four orientations. For any
// rectangle I find its tight bounding box
// with a 2D prefix sum, and try every cut
// position in every shape.

class Solution {
    fun minimumSum(grid: Array<IntArray>): Int {
        val m = grid.size
        val n = grid[0].size
        val ps = Array(m + 1) { IntArray(n + 1) }
        for (i in 0 until m) {
            var row = 0
            for (j in 0 until n) {
                row += grid[i][j]
                ps[i + 1][j + 1] = ps[i][j + 1] + row
            }
        }
        fun rectSum(top: Int, bottom: Int, left: Int, right: Int): Int {
            return ps[bottom][right] - ps[top][right] - ps[bottom][left] + ps[top][left]
        }
        fun area(top: Int, bottom: Int, left: Int, right: Int): Int {
            if (rectSum(top, bottom, left, right) == 0) return 0
            var minr = top
            while (rectSum(minr, minr + 1, left, right) == 0) minr++
            var maxr = bottom - 1
            while (rectSum(maxr, maxr + 1, left, right) == 0) maxr--
            var minc = left
            while (rectSum(top, bottom, minc, minc + 1) == 0) minc++
            var maxc = right - 1
            while (rectSum(top, bottom, maxc, maxc + 1) == 0) maxc--
            return (maxr - minr + 1) * (maxc - minc + 1)
        }
        var ans = Int.MAX_VALUE
        for (i in 1 until n - 1) {
            for (j in i + 1 until n) {
                ans = minOf(ans, area(0, m, 0, i) + area(0, m, i, j) + area(0, m, j, n))
            }
        }
        for (i in 1 until m - 1) {
            for (j in i + 1 until m) {
                ans = minOf(ans, area(0, i, 0, n) + area(i, j, 0, n) + area(j, m, 0, n))
            }
        }
        for (c in 1 until n) {
            for (r in 1 until m) {
                ans = minOf(ans, area(0, r, 0, c) + area(r, m, 0, c) + area(0, m, c, n))
                ans = minOf(ans, area(0, m, 0, c) + area(0, r, c, n) + area(r, m, c, n))
            }
        }
        for (r in 1 until m) {
            for (c in 1 until n) {
                ans = minOf(ans, area(0, r, 0, c) + area(0, r, c, n) + area(r, m, 0, n))
                ans = minOf(ans, area(0, r, 0, n) + area(r, m, 0, c) + area(r, m, c, n))
            }
        }
        return ans
    }
}
