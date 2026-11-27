// LeetCode 3699. Number of ZigZag Arrays I — Hard
// https://leetcode.com/problems/number-of-zigzag-arrays-i/
// Submission 2203048794 — Accepted, Kotlin
class Solution {
    fun zigZagArrays(n: Int, l: Int, r: Int): Int {
        // My thinking: only the direction of the last step matters.
        // For each possible last value I keep two counts: arrays
        // whose last step went up into it, and arrays whose last
        // step went down into it. An upward step may only follow
        // a downward one and vice versa, so each new count is a
        // prefix sum (for up) or a suffix sum (for down) of the
        // opposite direction's counts — no equal neighbours, and
        // three in a row can never run strictly up or down.
        val mod = 1_000_000_007L
        val m = r - l + 1
        // Length 2: up[v] counts smaller values, down[v] larger ones.
        var up = LongArray(m) { it.toLong() }
        var down = LongArray(m) { (m - 1 - it).toLong() }
        for (len in 3..n) {
            val newUp = LongArray(m)
            val newDown = LongArray(m)
            var s = 0L
            for (v in 0 until m) {
                newUp[v] = s
                s = (s + down[v]) % mod
            }
            s = 0L
            for (v in m - 1 downTo 0) {
                newDown[v] = s
                s = (s + up[v]) % mod
            }
            up = newUp
            down = newDown
        }
        var total = 0L
        for (v in 0 until m) total = (total + up[v] + down[v]) % mod
        return total.toInt()
    }
}
