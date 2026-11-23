// LeetCode 2468. Split Message Based on Limit — Hard
// https://leetcode.com/problems/split-message-based-on-limit/
// Submission 2201766535 — Accepted, Kotlin
//
// My thinking: the suffix "<a/b>" eats a
// different number of characters depending
// on how many digits a and b have, so I
// try the smallest part-count first and
// add up exactly what each part can hold
// — the first count whose parts swallow
// the whole message is the answer.

class Solution {
    fun splitMessage(message: String, limit: Int): List<String> {
        val n = message.length
        fun suffixLen(a: Int, b: Int) = 3 + a.toString().length + b.toString().length
        for (b in 1..n) {
            val capacities = mutableListOf<Int>()
            var ok = true
            for (a in 1..b) {
                val cap = limit - suffixLen(a, b)
                if (cap <= 0) { ok = false; break }
                capacities.add(cap)
            }
            if (!ok) continue
            if (capacities.sum() < n) continue
            val parts = mutableListOf<String>()
            var idx = 0
            for (a in 1..b) {
                val take = minOf(capacities[a - 1], n - idx)
                parts.add(message.substring(idx, idx + take) + "<$a/$b>")
                idx += take
            }
            if (idx == n) return parts
        }
        return emptyList()
    }
}
