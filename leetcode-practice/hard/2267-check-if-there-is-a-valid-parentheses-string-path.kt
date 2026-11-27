// LeetCode 2267. Check if There Is a Valid Parentheses String Path — Hard
// https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/
// Submission 2201647214 — Accepted, Kotlin
//
// My thinking: a path is only alive while
// its balance never dips below zero, so I
// carry the set of balances each cell can
// still reach and ask whether zero survives
// to the far corner.

class Solution {
    fun hasValidPath(grid: Array<CharArray>): Boolean {
        val m = grid.size
        val n = grid[0].size
        if ((m + n - 1) % 2 == 1) return false
        if (grid[0][0] == ')' || grid[m - 1][n - 1] == '(') return false
        val maxBal = (m + n) / 2
        val dp = Array(m) { Array(n) { mutableSetOf<Int>() } }
        dp[0][0].add(1)
        for (i in 0 until m) {
            for (j in 0 until n) {
                if (i == 0 && j == 0) continue
                val balances = mutableSetOf<Int>()
                if (i > 0) balances.addAll(dp[i - 1][j])
                if (j > 0) balances.addAll(dp[i][j - 1])
                for (b in balances) {
                    if (grid[i][j] == '(') {
                        val nb = b + 1
                        if (nb <= maxBal) dp[i][j].add(nb)
                    } else {
                        val nb = b - 1
                        if (nb >= 0) dp[i][j].add(nb)
                    }
                }
            }
        }
        return 0 in dp[m - 1][n - 1]
    }
}
