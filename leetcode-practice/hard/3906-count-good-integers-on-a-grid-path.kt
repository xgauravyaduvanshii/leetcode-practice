// LeetCode 3906. Count Good Integers on a Grid Path — Hard
// https://leetcode.com/problems/count-good-integers-on-a-grid-path/
// Submission 2203376118 — Accepted, Kotlin
class Solution {
    fun countGoodIntegersOnPath(l: Long, r: Long, directions: String): Long {
        // My thinking: pad x to 16 digits and lay it row by
        // row into a 4x4 grid. The path starts at (0, 0)
        // and takes three D steps and three R steps, so it
        // visits 7 cells whose digit positions 4*row+col
        // strictly increase along the path — the first is
        // position 0 and the last is position 15. Only the
        // digits on those 7 positions matter, and they must
        // read non-decreasing in path order; every other
        // digit is free. Count the good numbers up to X
        // with a digit DP over the 16 positions, carrying
        // the tight flag and the previous path digit (the
        // scan meets the path positions in path order, so a
        // path digit only has to be at least the previous
        // one), then answer count(r) - count(l - 1).
        var row = 0
        var col = 0
        val path = mutableListOf(0)
        for (ch in directions) {
            if (ch == 'D') row++ else col++
            path.add(4 * row + col)
        }
        val pathSet = path.toSet()

        fun countUpto(x: Long): Long {
            if (x < 0) return 0
            val s = x.toString().padStart(16, '0')
            val memo = Array(17) { Array(2) { arrayOfNulls<Long>(11) } }
            fun dp(pos: Int, tight: Boolean, prev: Int): Long {
                if (pos == 16) return 1
                val t = if (tight) 1 else 0
                memo[pos][t][prev + 1]?.let { return it }
                val limit = if (tight) s[pos] - '0' else 9
                var total = 0L
                val onPath = pos in pathSet
                for (d in 0..limit) {
                    if (onPath && prev >= 0 && d < prev) continue
                    total += dp(pos + 1, tight && d == limit, if (onPath) d else prev)
                }
                memo[pos][t][prev + 1] = total
                return total
            }
            return dp(0, true, -1)
        }

        return countUpto(r) - countUpto(l - 1)
    }
}
