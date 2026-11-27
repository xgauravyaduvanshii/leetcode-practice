// LeetCode 3605. Minimum Stability Factor of Array — Hard
// https://leetcode.com/problems/minimum-stability-factor-of-array/
// Submission 2202870592 — Accepted, Kotlin
import kotlin.math.min

class Solution {
    fun minStable(nums: IntArray, maxC: Int): Int {
        // My thinking: a subarray is stable exactly when its GCD
        // is at least 2, so changing an element to 1 breaks every
        // window through it. For a target stability factor X, every
        // window of length X+1 must be broken, and the cheapest way
        // is greedy: scanning left to right, the first uncovered
        // stable window gets a 1 at its right end, which covers the
        // most future windows. That test is monotone in X, so I
        // binary search the smallest X I can afford. The window
        // GCDs come from the short list of distinct GCDs of
        // subarrays ending at each position.
        val n = nums.size
        fun gcd(a: Int, b: Int): Int {
            var x = a
            var y = b
            while (y != 0) {
                val t = x % y
                x = y
                y = t
            }
            return x
        }
        fun can(x: Int): Boolean {
            if (x == 0) return nums.count { it >= 2 } <= maxC
            if (x >= n) return true
            var count = 0
            var lastBreak = -1
            var gcds = mutableListOf<Pair<Int, Int>>()
            for (r in 0 until n) {
                val next = mutableListOf(Pair(nums[r], 1))
                for ((g, cnt) in gcds) {
                    val ng = gcd(g, nums[r])
                    if (ng == next.last().first) {
                        next[next.lastIndex] = Pair(ng, next.last().second + cnt)
                    } else {
                        next.add(Pair(ng, cnt))
                    }
                }
                gcds = next
                if (r >= x) {
                    val l = r - x
                    if (l <= lastBreak) continue
                    var offset = r - l
                    var g = gcds.last().first
                    var rem = offset
                    for ((gv, cnt) in gcds) {
                        if (rem < cnt) { g = gv; break }
                        rem -= cnt
                    }
                    if (g >= 2) {
                        count++
                        lastBreak = r
                        if (count > maxC) return false
                    }
                }
            }
            return count <= maxC
        }
        var lo = 0
        var hi = n
        var best = n
        while (lo <= hi) {
            val mid = (lo + hi) / 2
            if (can(mid)) {
                best = mid
                hi = mid - 1
            } else {
                lo = mid + 1
            }
        }
        return best
    }
}
