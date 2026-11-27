// LeetCode 2333. Minimum Sum of Squared Difference — Medium
// https://leetcode.com/problems/minimum-sum-of-squared-difference/
// Submission 2204710035 — Accepted, Kotlin
//
// My thinking: same idea as the Python version — binary-search the
// smallest cap t that k operations can reach, keep differences below t
// as they are, and spend the leftover operations pulling some t's down
// to t-1. Longs are used because the squared sum can exceed 32 bits.
class Solution {
    fun minSumSquareDiff(nums1: IntArray, nums2: IntArray, k1: Int, k2: Int): Long {
        val k = k1.toLong() + k2.toLong()
        val diffs = IntArray(nums1.size) { i -> kotlin.math.abs(nums1[i] - nums2[i]) }
        var sum = 0L
        for (d in diffs) sum += d
        if (sum <= k) return 0L
        var lo = 0
        var hi = diffs.max()
        while (lo < hi) {
            val mid = (lo + hi) / 2
            var cost = 0L
            for (d in diffs) if (d > mid) cost += (d - mid)
            if (cost <= k) hi = mid else lo = mid + 1
        }
        val t = lo
        var cost = 0L
        for (d in diffs) if (d > t) cost += (d - t)
        val leftover = k - cost
        var ans = 0L
        var m = 0L
        for (d in diffs) {
            if (d < t) ans += d.toLong() * d
            else m++
        }
        ans += (m - leftover) * t.toLong() * t + leftover * (t - 1).toLong() * (t - 1)
        return ans
    }
}
