// 3317. Find the Number of Possible Ways for an Event (Hard)
// https://leetcode.com/problems/find-the-number-of-possible-ways-for-an-event/
// Submission 2202325564 -- Accepted, Kotlin
class Solution {
    fun numberOfWays(n: Int, x: Int, y: Int): Int {
        // My thinking: fix the number k of non-empty stages. The performers
        // split into k non-empty unlabelled groups in S(n, k) ways (Stirling
        // numbers of the second kind), the k stages are chosen and ordered in
        // P(x, k) = x * (x-1) * ... * (x-k+1) ways, and each of the k bands
        // gets one of y scores, giving y^k. I sum that product over all k.
        val MOD = 1_000_000_007L
        val kMax = minOf(n, x)
        var stir = LongArray(kMax + 1)
        stir[0] = 1L
        for (i in 1..n) {
            val nxt = LongArray(kMax + 1)
            for (k in 1..minOf(i, kMax)) {
                nxt[k] = (k.toLong() * stir[k] + stir[k - 1]) % MOD
            }
            stir = nxt
        }
        var ans = 0L
        var perm = 1L
        var powY = 1L
        for (k in 1..kMax) {
            perm = perm * (x - k + 1) % MOD
            powY = powY * y % MOD
            ans = (ans + perm * stir[k] % MOD * powY) % MOD
        }
        return ans.toInt()
    }
}
