// LeetCode 3077. Maximum Strength of K Disjoint Subarrays — Hard
// https://leetcode.com/problems/maximum-strength-of-k-disjoint-subarrays/
// Submission 2201925558 — Accepted, Kotlin
//
// My thinking: the j-th subarray is
// weighted by (k - j + 1), with the sign
// flipping each time, so I build the
// answer one subarray at a time. For
// each count j I sweep the array once,
// keeping the best place the j-th
// subarray could have started — its
// earlier strength minus the weighted
// prefix before it — and either extend
// the best subarray so far or end a new
// one here. Prefix sums make every
// subarray sum a subtraction.

class Solution {
    fun maximumStrength(nums: IntArray, k: Int): Long {
        val n = nums.size
        val prefix = LongArray(n + 1)
        for (i in nums.indices) prefix[i + 1] = prefix[i] + nums[i]
        val negInf = Long.MIN_VALUE / 4
        // dpPrev[i]: best strength with j-1 subarrays in nums[..i].
        var dpPrev = LongArray(n) { 0L }
        for (j in 1..k) {
            val coef = (k - j + 1).toLong() * if (j % 2 == 1) 1L else -1L
            val dpCur = LongArray(n) { negInf }
            var best = negInf // best of dpPrev[s-1] - coef * prefix[s]
            for (i in 0 until n) {
                val prev = if (i > 0) dpPrev[i - 1] else if (j == 1) 0L else negInf
                val cand = prev - coef * prefix[i]
                if (cand > best) best = cand
                val value = coef * prefix[i + 1] + best
                dpCur[i] = if (i == 0) value else maxOf(dpCur[i - 1], value)
            }
            dpPrev = dpCur
        }
        return dpPrev[n - 1]
    }
}
