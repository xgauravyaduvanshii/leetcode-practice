class Solution {
    fun numWays(words: Array<String>, target: String): Int {
        // My thinking: a column can only give one letter, so
        // walk the columns left to right and grow the ways to
        // build more and more of the target.
        val MOD = 1_000_000_007L
        val m = words[0].length
        val freq = Array(m) { IntArray(26) }
        for (w in words) for (i in w.indices) freq[i][w[i] - 'a']++
        val dp = LongArray(target.length + 1)
        dp[0] = 1
        for (i in 0 until m) {
            for (j in target.length - 1 downTo 0) {
                dp[j + 1] = (dp[j + 1] + dp[j] * freq[i][target[j] - 'a']) % MOD
            }
        }
        return dp[target.length].toInt()
    }
}
