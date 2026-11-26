// LeetCode 4081. Prime Subset Selection II — Hard
// https://leetcode.com/problems/prime-subset-selection-ii/
// Submission 2203697188 — Accepted, Kotlin

class Solution {
    fun maxPrimeSubset(n: Int, s: Int): List<Int> {
        // My thinking: first sieve out all primes up to n.
        // Then it is a subset-sum problem over those primes:
        // we want the largest sum <= s that a subset of the
        // primes can reach, and among the subsets reaching
        // that sum, the one with the fewest primes. dp[i][t]
        // = the smallest number of primes among primes[i:]
        // whose sum is exactly t (INF if impossible). Fill
        // it backwards: for each prime p, either skip it or
        // take it (cost 1 + the best for t - p). The best
        // sum is the largest t <= s with dp[0][t] finite.
        // Then walk the primes in increasing order and take
        // a prime whenever the remaining sum can still be
        // reached with one fewer prime, which rebuilds a
        // smallest subset with that sum.
        val isPrime = BooleanArray(n + 1) { true }
        isPrime[0] = false
        if (n >= 1) isPrime[1] = false
        var i = 2
        while (i * i <= n) {
            if (isPrime[i]) {
                var j = i * i
                while (j <= n) {
                    isPrime[j] = false
                    j += i
                }
            }
            i++
        }
        val primes = ArrayList<Int>()
        for (x in 2..n) if (isPrime[x]) primes.add(x)
        val m = primes.size
        val INF = 1000000000
        val dp = Array(m + 1) { IntArray(s + 1) { INF } }
        dp[m][0] = 0
        for (idx in m - 1 downTo 0) {
            val p = primes[idx]
            for (t in 0..s) {
                var best = dp[idx + 1][t]
                if (t >= p && dp[idx + 1][t - p] + 1 < best) best = dp[idx + 1][t - p] + 1
                dp[idx][t] = best
            }
        }
        var bestSum = -1
        for (t in s downTo 1) if (dp[0][t] < INF) { bestSum = t; break }
        if (bestSum == -1) return emptyList()
        val ans = ArrayList<Int>()
        var rem = bestSum
        var need = dp[0][bestSum]
        for (idx in 0 until m) {
            if (need == 0) break
            val p = primes[idx]
            if (p <= rem && dp[idx + 1][rem - p] == need - 1) {
                ans.add(p)
                rem -= p
                need--
            }
        }
        return ans
    }
}
