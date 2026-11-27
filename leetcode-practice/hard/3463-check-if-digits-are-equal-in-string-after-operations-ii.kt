// LeetCode 3463. Check If Digits Are Equal in String After Operations II — Hard
// https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-ii/
// Submission 2202558945 — Accepted 684/684, Kotlin
class Solution {
    fun hasSameDigits(s: String): Boolean {
        // My thinking: each reduction is a Pascal-triangle
        // weighting, so after n - 2 rounds the two final digits
        // are sums of C(n-2, i) * s[i] and C(n-2, i) * s[i+1]
        // modulo 10. I get each binomial coefficient mod 10
        // with Lucas' theorem mod 2 and mod 5, combined by
        // the Chinese remainder theorem (10 is not prime, so
        // no direct modular inverse exists).
        val n = s.length
        val digits = IntArray(n) { s[it] - '0' }

        // Small binomial coefficients C(a, b) for a, b < 5.
        val small = Array(5) { IntArray(5) }
        for (a in 0 until 5) {
            small[a][0] = 1
            small[a][a] = 1
            for (b in 1 until a) {
                small[a][b] = small[a - 1][b - 1] + small[a - 1][b]
            }
        }

        fun binomMod10(N: Int, K: Int): Int {
            if (K < 0 || K > N) return 0
            // Mod 2: C(N, K) is odd exactly when K's set bits
            // are a subset of N's (Lucas in base 2).
            val r2 = if (K and N.inv() == 0) 1 else 0
            // Mod 5: Lucas in base 5.
            var r5 = 1
            var nn = N
            var kk = K
            while (nn > 0 || kk > 0) {
                val ni = nn % 5
                val ki = kk % 5
                if (ki > ni) {
                    r5 = 0
                    break
                }
                r5 = (r5 * small[ni][ki]) % 5
                nn /= 5
                kk /= 5
            }
            // CRT: the number mod 10 is r5 or r5 + 5, whichever
            // has parity r2.
            return if (r5 % 2 == r2) r5 else r5 + 5
        }

        val k = n - 2
        var first = 0
        var second = 0
        for (i in 0 until n - 1) {
            val c = binomMod10(k, i)
            first = (first + c * digits[i]) % 10
            second = (second + c * digits[i + 1]) % 10
        }
        return first == second
    }
}
