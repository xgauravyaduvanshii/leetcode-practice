// LeetCode 1840. Maximum Building Height — Hard
// https://leetcode.com/problems/maximum-building-height/
// Submission 2201196806 — Accepted, Kotlin
//
// My thinking: the first building is height zero
// and every restriction is a ceiling, so I tighten
// the ceilings against their neighbours in both
// directions and take the tallest peak between
// each pair — or past the last one.

class Solution {
    fun maxBuilding(n: Int, restrictions: Array<IntArray>): Int {
        val pts = mutableListOf(intArrayOf(1, 0))
        for (r in restrictions) pts.add(intArrayOf(r[0], r[1]))
        pts.sortBy { it[0] }
        for (i in 1 until pts.size) {
            val dist = pts[i][0] - pts[i - 1][0]
            pts[i][1] = minOf(pts[i][1], pts[i - 1][1] + dist)
        }
        for (i in pts.size - 2 downTo 0) {
            val dist = pts[i + 1][0] - pts[i][0]
            pts[i][1] = minOf(pts[i][1], pts[i + 1][1] + dist)
        }
        var ans = 0
        for (i in 1 until pts.size) {
            val dist = pts[i][0] - pts[i - 1][0]
            ans = maxOf(ans, (pts[i - 1][1] + pts[i][1] + dist) / 2)
        }
        ans = maxOf(ans, pts.last()[1] + (n - pts.last()[0]))
        return ans
    }
}
