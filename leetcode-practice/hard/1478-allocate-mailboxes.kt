class Solution {
    fun minDistance(houses: IntArray, k: Int): Int {
        // My thinking: sort the houses, then a mailbox always
        // sits on the middle house of its stretch — so the
        // cost of each stretch is known, and the rest is
        // splitting the street into k stretches.
        val sorted = houses.sorted()
        val n = sorted.size
        val cost = Array(n) { IntArray(n) }
        for (i in 0 until n) {
            for (j in i until n) {
                val mid = (i + j) / 2
                var sum = 0
                for (t in i..j) sum += kotlin.math.abs(sorted[t] - sorted[mid])
                cost[i][j] = sum
            }
        }
        val INF = Int.MAX_VALUE / 2
        val dp = Array(k + 1) { IntArray(n + 1) { INF } }
        dp[0][0] = 0
        for (boxes in 1..k) {
            for (end in 1..n) {
                for (start in 0 until end) {
                    if (dp[boxes - 1][start] != INF) {
                        dp[boxes][end] = minOf(dp[boxes][end], dp[boxes - 1][start] + cost[start][end - 1])
                    }
                }
            }
        }
        return dp[k][n]
    }
}
