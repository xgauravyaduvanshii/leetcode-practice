// LeetCode 3261. Count Substrings That Satisfy K-Constraint II — Hard
// https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii/
// Submission 2202158920 — Accepted, Kotlin
//
// My thinking: a substring is valid when not
// both 0s and 1s exceed k. Sliding a window
// gives, for each right end r, the smallest
// left end that keeps it valid — leftBound[r].
// A query [l, r] counts, for every right end,
// the valid left ends: ends whose bound is at
// most l contribute r' - l + 1 each, the rest
// contribute r' - bound + 1. Prefix sums over
// leftBound plus a binary search split the
// two groups in O(log n) per query.

class Solution {
    fun countKConstraintSubstrings(s: String, k: Int, queries: Array<IntArray>): LongArray {
        val n = s.length
        val leftBound = IntArray(n)
        var left = 0
        var cnt0 = 0
        var cnt1 = 0
        for (r in 0 until n) {
            if (s[r] == '0') cnt0++ else cnt1++
            while (cnt0 > k && cnt1 > k) {
                if (s[left] == '0') cnt0-- else cnt1--
                left++
            }
            leftBound[r] = left
        }
        val pref = LongArray(n + 1)
        for (i in 0 until n) pref[i + 1] = pref[i] + leftBound[i]
        val ans = LongArray(queries.size)
        for (qi in queries.indices) {
            val l = queries[qi][0]
            val r = queries[qi][1]
            val len = (r - l + 1).toLong()
            val sumB1 = (l + r).toLong() * len / 2 + len
            var lo = l
            var hi = r + 1
            while (lo < hi) {
                val mid = (lo + hi) / 2
                if (leftBound[mid] <= l) lo = mid + 1 else hi = mid
            }
            val pos = lo
            val cntLe = (pos - l).toLong()
            val sumLe = pref[pos] - pref[l]
            val sumTotal = pref[r + 1] - pref[l]
            val sumMax = cntLe * l + (sumTotal - sumLe)
            ans[qi] = sumB1 - sumMax
        }
        return ans
    }
}
