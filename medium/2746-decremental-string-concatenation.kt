// LeetCode 2746. Decremental String Concatenation — Medium
// https://leetcode.com/problems/decremental-string-concatenation/
// Submission 2205237941 — Accepted, Kotlin
//
// My thinking: same idea as the Python version — DP over the
// first and last letters of the string built so far; each new
// word is appended or prepended, saving 1 when the touching
// letters match.
class Solution {
    fun minimizeConcatenatedLength(words: Array<String>): Int {
        val INF = 1_000_000_000
        var dp = Array(26) { IntArray(26) { INF } }
        val first = words[0][0] - 'a'
        val last = words[0][words[0].length - 1] - 'a'
        dp[first][last] = words[0].length
        for (wi in 1 until words.size) {
            val w = words[wi]
            val f = w[0] - 'a'
            val l = w[w.length - 1] - 'a'
            val ndp = Array(26) { IntArray(26) { INF } }
            for (a in 0 until 26) {
                for (b in 0 until 26) {
                    if (dp[a][b] == INF) continue
                    // Append w after the current string.
                    ndp[a][l] = minOf(ndp[a][l], dp[a][b] + w.length - if (b == f) 1 else 0)
                    // Prepend w before the current string.
                    ndp[f][b] = minOf(ndp[f][b], dp[a][b] + w.length - if (l == a) 1 else 0)
                }
            }
            dp = ndp
        }
        return dp.minOf { row -> row.min() }
    }
}
