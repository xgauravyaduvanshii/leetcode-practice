// LeetCode 4046. Minimum Cost Path With At Most K Turns — Hard
// https://leetcode.com/problems/minimum-cost-path-with-at-most-k-turns/
// Submission 2203532400 — Accepted, Kotlin
class Solution {
    fun minCost(grid: Array<IntArray>, k: Int): Int {
        // My thinking: a path with t turns is t+1 straight
        // runs, so track cost by (cell, last direction,
        // turns used), with directions 0 up, 1 down, 2 left,
        // 3 right, in cost[d][i][j]. Moving straight never
        // changes the turn count or the direction, so inside
        // one turn layer and one direction the moves run
        // along a single row or column in one direction — a
        // prefix minimum: the cheapest way to be at a cell
        // moving right is the grid cost plus the cheaper of
        // continuing the run from the left neighbour or
        // turning into this run at that neighbour from the
        // layer below. Sweep each direction in its own order
        // (right left-to-right, left right-to-left, down
        // top-to-bottom, up bottom-to-top), carrying the run
        // in one variable. Layer 0 starts at the start cell
        // with any last direction, since the first move is
        // free; each later layer turns once more. The answer
        // is the best over all layers up to k and all four
        // last directions at the target, or -1 when nothing
        // reaches it. Costs are Long so a whole path fits
        // easily; INF is far from overflow when a cell cost
        // is added.
        val m = grid.size
        val n = grid[0].size
        val INF = Long.MAX_VALUE / 4

        fun layer(prev: Array<Array<LongArray>>?): Array<Array<LongArray>> {
            val cur = Array(4) { Array(m) { LongArray(n) { INF } } }
            if (prev == null) {
                for (d in 0..3) cur[d][0][0] = grid[0][0].toLong()
            }
            for (i in 0 until m) {
                var run = cur[3][i][0]
                for (j in 1 until n) {
                    var best = run
                    if (prev != null) {
                        val turn = minOf(prev[0][i][j - 1], prev[1][i][j - 1], prev[2][i][j - 1])
                        if (turn < best) best = turn
                    }
                    cur[3][i][j] = grid[i][j] + best
                    run = cur[3][i][j]
                }
            }
            for (i in 0 until m) {
                var run = cur[2][i][n - 1]
                for (j in n - 2 downTo 0) {
                    var best = run
                    if (prev != null) {
                        val turn = minOf(prev[0][i][j + 1], prev[1][i][j + 1], prev[3][i][j + 1])
                        if (turn < best) best = turn
                    }
                    cur[2][i][j] = grid[i][j] + best
                    run = cur[2][i][j]
                }
            }
            for (j in 0 until n) {
                var run = cur[1][0][j]
                for (i in 1 until m) {
                    var best = run
                    if (prev != null) {
                        val turn = minOf(prev[0][i - 1][j], prev[2][i - 1][j], prev[3][i - 1][j])
                        if (turn < best) best = turn
                    }
                    cur[1][i][j] = grid[i][j] + best
                    run = cur[1][i][j]
                }
            }
            for (j in 0 until n) {
                var run = cur[0][m - 1][j]
                for (i in m - 2 downTo 0) {
                    var best = run
                    if (prev != null) {
                        val turn = minOf(prev[1][i + 1][j], prev[2][i + 1][j], prev[3][i + 1][j])
                        if (turn < best) best = turn
                    }
                    cur[0][i][j] = grid[i][j] + best
                    run = cur[0][i][j]
                }
            }
            if (prev == null) {
                for (d in 0..3) cur[d][0][0] = grid[0][0].toLong()
            }
            return cur
        }

        var prev = layer(null)
        var ans = minOf(prev[0][m - 1][n - 1], prev[1][m - 1][n - 1], prev[2][m - 1][n - 1], prev[3][m - 1][n - 1])
        for (t in 1..k) {
            prev = layer(prev)
            val cur = minOf(prev[0][m - 1][n - 1], prev[1][m - 1][n - 1], prev[2][m - 1][n - 1], prev[3][m - 1][n - 1])
            if (cur < ans) ans = cur
        }
        return if (ans >= INF / 2) -1 else ans.toInt()
    }
}
