// LeetCode 2547. Minimum Cost to Split an Array — Hard
// https://leetcode.com/problems/minimum-cost-to-split-an-array/
// Submission 2201808600 — Accepted, Kotlin
//
// My thinking: I cut the array from the
// left, and for each new cut I stretch
// the last piece rightward, keeping a
// running count of how many of its
// numbers show up at least twice — that
// count plus k is the piece's price, and
// the cheapest cut wins.

class Solution {
    fun minCost(nums: IntArray, k: Int): Int {
        val n = nums.size
        val INF = Int.MAX_VALUE / 2
        val dp = IntArray(n + 1) { INF }
        dp[0] = 0
        for (i in 1..n) {
            val freq = HashMap<Int, Int>()
            var trimmed = 0
            for (j in i - 1 downTo 0) {
                val x = nums[j]
                val c = (freq[x] ?: 0) + 1
                freq[x] = c
                if (c == 2) trimmed += 2
                else if (c > 2) trimmed += 1
                dp[i] = minOf(dp[i], dp[j] + k + trimmed)
            }
        }
        return dp[n]
    }
}
