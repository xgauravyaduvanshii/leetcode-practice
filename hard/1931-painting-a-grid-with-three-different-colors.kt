// LeetCode 1931. Painting a Grid With Three Different Colors — Hard
// https://leetcode.com/problems/painting-a-grid-with-three-different-colors/
// Submission 2201244059 — Accepted, Kotlin
//
// My thinking: a column is one of a few colourings
// with no two neighbours equal, so I list them all
// and count the ways to stack compatible columns
// one after another.

class Solution {
    fun colorTheGrid(m: Int, n: Int): Int {
        val MOD = 1_000_000_007L
        val patterns = mutableListOf<IntArray>()
        val cur = IntArray(m)
        fun gen(pos: Int) {
            if (pos == m) {
                patterns.add(cur.copyOf())
                return
            }
            for (c in 0..2) {
                if (pos == 0 || cur[pos - 1] != c) {
                    cur[pos] = c
                    gen(pos + 1)
                }
            }
        }
        gen(0)
        val k = patterns.size
        val compat = Array(k) { mutableListOf<Int>() }
        for (i in 0 until k) {
            for (j in 0 until k) {
                if ((0 until m).all { patterns[i][it] != patterns[j][it] }) {
                    compat[i].add(j)
                }
            }
        }
        var dp = LongArray(k) { 1L }
        for (col in 1 until n) {
            val ndp = LongArray(k)
            for (i in 0 until k) {
                var sum = 0L
                for (j in compat[i]) {
                    sum = (sum + dp[j]) % MOD
                }
                ndp[i] = sum
            }
            dp = ndp
        }
        return (dp.sum() % MOD).toInt()
    }
}
