// LeetCode 2328. Number of Increasing Paths in a Grid — Hard
// https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/
// Submission 2201683815 — Accepted, Kotlin
//
// My thinking: every cell starts a path of
// its own and grows into each taller
// neighbour — I memoise how many paths
// each cell begins and add them all up.

class Solution {
    private val MOD = 1_000_000_007
    private lateinit var grid: Array<IntArray>
    private lateinit var dp: Array<IntArray>
    private var m = 0
    private var n = 0

    fun countPaths(grid: Array<IntArray>): Int {
        this.grid = grid
        m = grid.size
        n = grid[0].size
        dp = Array(m) { IntArray(n) }
        var ans = 0
        for (i in 0 until m) {
            for (j in 0 until n) {
                ans = (ans + dfs(i, j)) % MOD
            }
        }
        return ans
    }

    private fun dfs(i: Int, j: Int): Int {
        if (dp[i][j] != 0) return dp[i][j]
        var total = 1L
        val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
        for ((di, dj) in dirs) {
            val ni = i + di
            val nj = j + dj
            if (ni in 0 until m && nj in 0 until n && grid[ni][nj] > grid[i][j]) {
                total = (total + dfs(ni, nj)) % MOD
            }
        }
        dp[i][j] = total.toInt()
        return dp[i][j]
    }
}
