// LeetCode 3116. Kth Smallest Amount With Single Denomination Combination — Hard
// https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/
// Submission 2202005565 — Accepted, Kotlin
//
// My thinking: I drop any coin that is
// a multiple of a smaller one, then
// build all subset LCMs with
// inclusion-exclusion signs. Those tell
// me how many numbers up to x are
// divisible by at least one coin, and
// that count only grows with x, so I
// binary-search the smallest x whose
// count reaches k.

class Solution {
    fun findKthSmallest(coins: IntArray, k: Int): Long {
        val filt = mutableListOf<Long>()
        for (c in coins.distinct().sorted()) {
            val cl = c.toLong()
            if (filt.any { cl % it == 0L }) continue
            filt.add(cl)
        }
        var hi = k.toLong() * filt[0]
        val pairs = mutableListOf<Pair<Long, Long>>()
        for (c in filt) {
            val newPairs = mutableListOf<Pair<Long, Long>>()
            newPairs.add(Pair(c, 1L))
            for ((l, s) in pairs) {
                val nl = l / gcd(l, c) * c
                if (nl <= hi) newPairs.add(Pair(nl, -s))
            }
            pairs.addAll(newPairs)
        }
        fun count(x: Long): Long {
            var total = 0L
            for ((l, s) in pairs) total += s * (x / l)
            return total
        }
        var lo = 1L
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (count(mid) >= k) hi = mid else lo = mid + 1
        }
        return lo
    }
    private fun gcd(a: Long, b: Long): Long {
        var x = a
        var y = b
        while (y != 0L) {
            val t = x % y
            x = y
            y = t
        }
        return x
    }
}
