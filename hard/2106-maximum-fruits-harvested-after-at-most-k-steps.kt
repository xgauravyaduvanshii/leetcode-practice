// LeetCode 2106. Maximum Fruits Harvested After at Most K Steps — Hard
// https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/
// Submission 2201576161 — Accepted, Kotlin
//
// My thinking: a walk that covers a stretch of
// fruit goes one way first and then back, so
// the cheapest way to cover any stretch is the
// shorter of the two turnarounds — and as the
// right end moves out, the left end only ever
// moves out too, so one sliding window finds
// the richest stretch.

class Solution {
    fun maxTotalFruits(fruits: Array<IntArray>, startPos: Int, k: Int): Int {
        val n = fruits.size
        val prefix = IntArray(n + 1)
        for (i in 0 until n) prefix[i + 1] = prefix[i] + fruits[i][1]

        fun steps(l: Int, r: Int): Int {
            val lp = fruits[l][0]
            val rp = fruits[r][0]
            if (rp <= startPos) return startPos - lp
            if (lp >= startPos) return rp - startPos
            val goLeftFirst = 2 * (startPos - lp) + (rp - startPos)
            val goRightFirst = 2 * (rp - startPos) + (startPos - lp)
            return minOf(goLeftFirst, goRightFirst)
        }

        var ans = 0
        var left = 0
        for (right in 0 until n) {
            while (left <= right && steps(left, right) > k) left++
            ans = maxOf(ans, prefix[right + 1] - prefix[left])
        }
        return ans
    }
}
