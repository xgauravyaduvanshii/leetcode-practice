// LeetCode 1883. Minimum Skips to Arrive at Meeting On Time — Hard
// https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/
// Submission 2201216140 — Accepted, Kotlin
//
// My thinking: I walk the roads keeping, for
// every number of skips used, the earliest I can
// arrive — skipping a rest just carries the raw
// driving time forward, resting rounds it up to
// the next whole hour.

import kotlin.math.ceil

class Solution {
    fun minSkips(dist: IntArray, speed: Int, hoursBefore: Double): Int {
        val n = dist.size
        val INF = Double.POSITIVE_INFINITY
        var dp = DoubleArray(n + 1) { INF }
        dp[0] = 0.0
        for (i in dist.indices) {
            val ndp = DoubleArray(n + 1) { INF }
            for (j in 0..n) {
                if (dp[j] == INF) continue
                val t = dp[j] + dist[i].toDouble() / speed
                if (i < n - 1) {
                    ndp[j] = minOf(ndp[j], ceil(t - 1e-9))
                } else {
                    ndp[j] = minOf(ndp[j], t)
                }
                if (j + 1 <= n) {
                    ndp[j + 1] = minOf(ndp[j + 1], t)
                }
            }
            dp = ndp
        }
        for (j in 0..n) {
            if (dp[j] <= hoursBefore + 1e-9) return j
        }
        return -1
    }
}
