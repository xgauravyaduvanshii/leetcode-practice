// LeetCode 3287. Find the Maximum Sequence Value of Array — Hard
// https://leetcode.com/problems/find-the-maximum-sequence-value-of-array/
// Submission 2202181900 — Accepted, Kotlin
//
// My thinking: split the array at some point,
// take k elements from the left part and k from
// the right, and maximise OR(left) XOR OR(right).
// For each side I keep the set of every OR value
// reachable with exactly k picks, built prefix
// by prefix and suffix by suffix. Then every
// split pairs the reachable ORs from its prefix
// and suffix.

class Solution {
    fun maxValue(nums: IntArray, k: Int): Int {
        val n = nums.size
        val pref = Array(n) { mutableSetOf<Int>() }
        var dp = Array(k + 1) { mutableSetOf<Int>() }
        dp[0].add(0)
        for (i in nums.indices) {
            val x = nums[i]
            val up = minOf(i + 1, k)
            for (t in up downTo 1) {
                if (dp[t - 1].isNotEmpty()) {
                    val add = dp[t - 1].map { it or x }
                    dp[t].addAll(add)
                }
            }
            pref[i] = dp[k].toMutableSet()
        }
        val suff = Array(n) { mutableSetOf<Int>() }
        dp = Array(k + 1) { mutableSetOf<Int>() }
        dp[0].add(0)
        for (i in n - 1 downTo 0) {
            val x = nums[i]
            val up = minOf(n - i, k)
            for (t in up downTo 1) {
                if (dp[t - 1].isNotEmpty()) {
                    val add = dp[t - 1].map { it or x }
                    dp[t].addAll(add)
                }
            }
            suff[i] = dp[k].toMutableSet()
        }
        var ans = 0
        for (i in 0 until n - 1) {
            for (a in pref[i]) {
                for (b in suff[i + 1]) {
                    ans = maxOf(ans, a xor b)
                }
            }
        }
        return ans
    }
}
