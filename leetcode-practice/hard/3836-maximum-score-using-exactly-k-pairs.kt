// LeetCode 3836. Maximum Score Using Exactly K Pairs — Hard
// https://leetcode.com/problems/maximum-score-using-exactly-k-pairs/
// Submission 2203282673 — Accepted, Kotlin
class Solution {
    fun maxScore(nums1: IntArray, nums2: IntArray, k: Int): Long {
        // My thinking: dp[t][i][j] is the best score using
        // exactly t pairs inside the first i entries of nums1
        // and the first j of nums2. Either skip nums1[i-1],
        // skip nums2[j-1], or take the pair (i-1, j-1) as the
        // last pair on top of the best t-1 pairs before it.
        // Impossible states stay at negative infinity, which
        // matters because products can be negative and taking
        // a bad pair can still beat leaving the count short.
        // The answer is dp[k][n][m]. Scores use Long because
        // a product of two entries can reach 10^12.
        val n = nums1.size
        val m = nums2.size
        val NEG = Long.MIN_VALUE / 4
        val dp = Array(k + 1) { Array(n + 1) { LongArray(m + 1) { NEG } } }
        for (i in 0..n) {
            for (j in 0..m) {
                dp[0][i][j] = 0L
            }
        }
        for (t in 1..k) {
            for (i in 1..n) {
                for (j in 1..m) {
                    var best = maxOf(dp[t][i - 1][j], dp[t][i][j - 1])
                    val prev = dp[t - 1][i - 1][j - 1]
                    if (prev != NEG) {
                        best = maxOf(best, prev + nums1[i - 1].toLong() * nums2[j - 1].toLong())
                    }
                    dp[t][i][j] = best
                }
            }
        }
        return dp[k][n][m]
    }
}
