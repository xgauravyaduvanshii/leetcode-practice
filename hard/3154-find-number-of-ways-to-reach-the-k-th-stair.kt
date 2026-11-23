// LeetCode 3154. Find Number of Ways to Reach the K-th Stair — Hard
// https://leetcode.com/problems/find-number-of-ways-to-reach-the-k-th-stair/
// Submission 2202045694 — Accepted, Kotlin
//
// My thinking: to reach stair k I must
// jump to some 2^x >= k, then step down
// y = 2^x - k times. The jumps and steps
// can interleave in C(x + 1, y) ways, and
// only finitely many x work — once y
// exceeds x + 1 there are no more. I sum
// the combinations over all valid x.

class Solution {
    fun waysToReachStair(k: Int): Int {
        var ans = 0L
        var x = 0
        while (true) {
            val y = (1L shl x) - k
            if (y < 0) {
                x++
                continue
            }
            if (y > x + 1) break
            ans += comb(x + 1, y.toInt())
            x++
        }
        return ans.toInt()
    }

    private fun comb(n: Int, r0: Int): Long {
        var r = r0
        if (r < 0 || r > n) return 0L
        if (r > n - r) r = n - r
        var res = 1L
        for (i in 1..r) {
            res = res * (n - r + i) / i
        }
        return res
    }
}
