// LeetCode 3490. Count Beautiful Numbers — Hard
// https://leetcode.com/problems/count-beautiful-numbers/
// Submission 2202711857 — Accepted, Kotlin
class Solution {
    fun beautifulNumbers(l: Int, r: Int): Int {
        // My thinking: a number is beautiful when its digit product
        // is a multiple of its digit sum. A zero digit makes the
        // product 0, which is a multiple of any sum, so those numbers
        // are all beautiful. I count numbers up to X by fixing the
        // digit sum s (at most 9 * 9 = 81) and running a digit DP
        // that tracks the product modulo s and the running sum.
        // The digit is always added to the sum, even after the
        // product has become 0 — skipping that update undercounts
        // the sum for numbers like 101. The answer is
        // count(r) - count(l - 1).
        fun count(X: Int): Int {
            if (X <= 0) return 0
            val digits = X.toString().map { it - '0' }
            val n = digits.size
            var total = 0
            for (target in 1..9 * n) {
                // memo[pos][prodMod][sum][started] = -1 uncomputed
                val memo = Array(n + 1) { Array(target) { Array(target + 1) { IntArray(2) { -1 } } } }
                fun dp(pos: Int, prodMod: Int, sum: Int, tight: Boolean, started: Boolean): Int {
                    if (pos == n) {
                        return if (started && sum == target && prodMod == 0) 1 else 0
                    }
                    val sIdx = if (started) 1 else 0
                    if (!tight && memo[pos][prodMod][sum][sIdx] != -1) {
                        return memo[pos][prodMod][sum][sIdx]
                    }
                    val limit = if (tight) digits[pos] else 9
                    var ans = 0
                    for (d in 0..limit) {
                        val ntight = tight && d == limit
                        if (!started && d == 0) {
                            ans += dp(pos + 1, prodMod, sum, ntight, false)
                        } else {
                            val nsum = sum + d
                            if (nsum > target) continue
                            val nprod = if (!started) d % target else (prodMod * d) % target
                            ans += dp(pos + 1, nprod, nsum, ntight, true)
                        }
                    }
                    if (!tight) memo[pos][prodMod][sum][sIdx] = ans
                    return ans
                }
                total += dp(0, 0, 0, true, false)
            }
            return total
        }
        return count(r) - count(l - 1)
    }
}
