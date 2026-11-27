// LeetCode 1799. Maximize Score After N Operations — Hard
// https://leetcode.com/problems/maximize-score-after-n-operations/
// Submission 2201170593 — Accepted, Kotlin
//
// My thinking: I remember which numbers are already
// used as a bitmask, and at each step I try every
// unused pair — the pair's score is the operation
// number times the gcd of the two numbers.

import kotlin.math.max

class Solution {
    fun maxScore(nums: IntArray): Int {
        val n = nums.size
        val m = 1 shl n
        val dp = IntArray(m)
        for (mask in 0 until m) {
            val bits = Integer.bitCount(mask)
            if (bits % 2 == 1) continue
            val op = bits / 2 + 1
            for (i in 0 until n) {
                if (mask and (1 shl i) != 0) continue
                for (j in i + 1 until n) {
                    if (mask and (1 shl j) != 0) continue
                    val nmask = mask or (1 shl i) or (1 shl j)
                    dp[nmask] = max(dp[nmask], dp[mask] + op * gcd(nums[i], nums[j]))
                }
            }
        }
        return dp[m - 1]
    }

    private fun gcd(a: Int, b: Int): Int = if (b == 0) a else gcd(b, a % b)
}
