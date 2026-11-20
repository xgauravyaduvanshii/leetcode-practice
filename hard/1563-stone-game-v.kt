class Solution {
    fun stoneGameV(stoneValue: IntArray): Int {
        // My thinking: split the pile in two — keep the
        // smaller side's sum and play on with it, or take the
        // better side when both weigh the same.
        val n = stoneValue.size
        val prefix = IntArray(n + 1)
        for (i in stoneValue.indices) prefix[i + 1] = prefix[i] + stoneValue[i]
        fun total(l: Int, r: Int): Int = prefix[r + 1] - prefix[l]
        val memo = Array(n) { IntArray(n) { -1 } }
        fun dp(l: Int, r: Int): Int {
            if (l == r) return 0
            if (memo[l][r] != -1) return memo[l][r]
            var best = 0
            for (k in l until r) {
                val left = total(l, k)
                val right = total(k + 1, r)
                if (left < right) best = maxOf(best, left + dp(l, k))
                else if (left > right) best = maxOf(best, right + dp(k + 1, r))
                else best = maxOf(best, left + dp(l, k), right + dp(k + 1, r))
            }
            memo[l][r] = best
            return best
        }
        return dp(0, n - 1)
    }
}
