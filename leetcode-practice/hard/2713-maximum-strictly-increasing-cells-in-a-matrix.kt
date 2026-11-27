// LeetCode 2713. Maximum Strictly Increasing Cells in a Matrix — Hard
// https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/
// Submission 2201876694 — Accepted, Kotlin
//
// My thinking: a cell can only follow
// a strictly smaller one in its row or
// column, so I visit the cells in
// increasing order of value, each one
// reaching back to the best chain its
// row or column has seen so far — and
// cells of the same value are settled
// together, so none of them can borrow
// from another of its own kind.

class Solution {
    fun maxIncreasingCells(mat: Array<IntArray>): Int {
        val m = mat.size
        val n = mat[0].size
        val cells = mutableMapOf<Int, MutableList<Pair<Int, Int>>>()
        for (i in 0 until m) {
            for (j in 0 until n) {
                cells.getOrPut(mat[i][j]) { mutableListOf() }.add(Pair(i, j))
            }
        }
        val rowBest = IntArray(m)
        val colBest = IntArray(n)
        var ans = 0
        for (v in cells.keys.sorted()) {
            val group = cells[v]!!
            val dps = group.map { (i, j) ->
                val d = 1 + maxOf(rowBest[i], colBest[j])
                ans = maxOf(ans, d)
                d
            }
            for ((idx, cell) in group.withIndex()) {
                val (i, j) = cell
                rowBest[i] = maxOf(rowBest[i], dps[idx])
                colBest[j] = maxOf(colBest[j], dps[idx])
            }
        }
        return ans
    }
}
