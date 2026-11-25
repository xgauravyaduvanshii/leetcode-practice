// LeetCode 3666. Minimum Operations to Equalize Binary String — Hard
// https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/
// Submission 2203024495 — Accepted, Kotlin
class Solution {
    fun minOperations(s: String, k: Int): Int {
        // My thinking: with t operations I flip t * k bits in total.
        // Every '0' must be flipped an odd number of times and every
        // '1' an even number of times, so t * k must have the same
        // parity as the number of zeroes, and the zeroes need at
        // least one flip each. A single position can only be flipped
        // once per operation, so the zeroes can absorb at most
        // z * t flips when t is odd (z * (t - 1) when t is even,
        // since an odd count can never reach t), and the same cap
        // holds for the ones; each operation also has to flip at
        // least k - (n - z) zeroes because there are only that many
        // ones to fill the rest. I try t = 1, 2, 3, ... and take the
        // first t where some flip count a for the zeroes fits all
        // of those bounds with the right parity — that t is minimal,
        // and if no t fits the string can never become all '1's.
        val n = s.length
        val z = s.count { it == '0' }.toLong()
        if (z == 0L) return 0
        val kk = k.toLong()
        val ones = (n - z).toLong()
        for (t in 1..1_000_000) {
            val tt = t.toLong()
            if ((tt * kk - z) % 2 != 0L) continue
            val onesCap = ones * (if (t % 2 == 0) tt else tt - 1)
            val zeroCap = z * (if (t % 2 == 1) tt else tt - 1)
            val lo = maxOf(z, tt * maxOf(0L, kk - ones), tt * kk - onesCap)
            val hi = minOf(tt * minOf(kk, z), zeroCap)
            if (lo > hi) continue
            val a = if (lo % 2 == z % 2) lo else lo + 1
            if (a <= hi) return t
        }
        return -1
    }
}
