// LeetCode 3538. Merge Operations for Minimum Travel Time — Hard
// https://leetcode.com/problems/merge-operations-for-minimum-travel-time/
// Submission 2202816839 — Accepted, Kotlin
class Solution {
    fun minTravelTime(l: Int, n: Int, k: Int, position: IntArray, time: IntArray): Int {
        // My thinking: merging joins neighbouring signs into groups,
        // and a group's time is the sum of its signs' times while its
        // representative is its rightmost sign. The road then costs,
        // for each group except the last, the distance to the next
        // group's representative times that group's time sum. A
        // group's cost is only known once the next representative is
        // chosen, so my DP state keeps the last two representatives:
        // dp[prev][i][g] is the cheapest cost for groups ending at i,
        // counting every segment except the one starting at i, and
        // extending to a new representative j adds the segment
        // [position[i], position[j]] at the group ending at i.
        val INF = Int.MAX_VALUE / 4
        val pref = IntArray(n + 1)
        for (i in 0 until n) pref[i + 1] = pref[i] + time[i]
        val groupsNeeded = n - k
        val dp = Array(n + 1) { Array(n) { IntArray(groupsNeeded + 1) { INF } } }
        dp[0][0][1] = 0
        for (i in 0 until n) {
            for (prevIdx in 0..n) {
                val prev = prevIdx - 1
                if (prev >= i) continue
                for (g in 1..groupsNeeded) {
                    val cur = dp[prevIdx][i][g]
                    if (cur == INF) continue
                    val s = pref[i + 1] - pref[prev + 1]
                    for (j in i + 1 until n) {
                        if (g + 1 > groupsNeeded) break
                        val nv = cur + (position[j] - position[i]) * s
                        if (nv < dp[i + 1][j][g + 1]) dp[i + 1][j][g + 1] = nv
                    }
                }
            }
        }
        var ans = INF
        for (prevIdx in 0..n) ans = minOf(ans, dp[prevIdx][n - 1][groupsNeeded])
        return ans
    }
}
