class Solution {
    fun minimumDistance(word: String): Int {
        // My thinking: one finger always sits on the last letter
        // typed, so only the other finger's position matters —
        // keep the cheapest cost for each spot it could be.
        fun dist(a: Int, b: Int): Int {
            if (a == 27 || b == 27) return 0
            return Math.abs(a / 6 - b / 6) + Math.abs(a % 6 - b % 6)
        }
        val n = word.length
        val INF = Int.MAX_VALUE / 2
        var dp = IntArray(28) { INF }
        dp[27] = 0
        for (i in 1 until n) {
            val cur = IntArray(28) { INF }
            val prevChar = word[i - 1] - 'A'
            val char = word[i] - 'A'
            for (other in 0 until 28) {
                if (dp[other] == INF) continue
                cur[other] = minOf(cur[other], dp[other] + dist(prevChar, char))
                cur[prevChar] = minOf(cur[prevChar], dp[other] + dist(other, char))
            }
            dp = cur
        }
        return dp.minOrNull() ?: 0
    }
}
