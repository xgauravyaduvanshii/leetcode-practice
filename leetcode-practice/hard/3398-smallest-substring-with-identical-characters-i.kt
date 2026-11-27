// LeetCode 3398. Smallest Substring With Identical Characters I — Hard
// https://leetcode.com/problems/smallest-substring-with-identical-characters-i/
// Submission 2202507201 — Accepted 949/949, Kotlin
//
class Solution {
    fun minLength(s: String, numOps: Int): Int {
        // My thinking: binary-search the answer L. For a fixed L,
        // the cheapest way to keep every run at most L long is a
        // left-to-right DP: the last run of the answer is one block
        // of equal characters, so the cost of ending at i with a
        // given character is the cost of that block plus the best
        // cost of the prefix before it ending in the other
        // character. The block cost is a difference of prefix
        // counts, so the best previous split is a sliding-window
        // minimum over the last L positions — two deques make the
        // whole check O(n).
        val n = s.length
        // nc0[i] / nc1[i]: number of '1's / '0's in s[:i].
        val nc0 = IntArray(n + 1)
        val nc1 = IntArray(n + 1)
        for (i in s.indices) {
            nc0[i + 1] = nc0[i] + if (s[i] == '1') 1 else 0
            nc1[i + 1] = nc1[i] + if (s[i] == '0') 1 else 0
        }

        fun minFlips(limit: Int): Int {
            // v0[j + 1] = best cost of a prefix ending at j with a
            // '1', minus nc0[j + 1]; v1 is the mirror image.
            val v0 = IntArray(n + 1)
            val v1 = IntArray(n + 1)
            val dq0 = ArrayDeque<Int>()
            val dq1 = ArrayDeque<Int>()
            dq0.addLast(-1)
            dq1.addLast(-1)
            var best0 = 0
            var best1 = 0
            for (i in 0 until n) {
                while (dq0.first() < i - limit) dq0.removeFirst()
                while (dq1.first() < i - limit) dq1.removeFirst()
                best0 = nc0[i + 1] + v0[dq0.first() + 1]
                best1 = nc1[i + 1] + v1[dq1.first() + 1]
                v0[i + 1] = best1 - nc0[i + 1]
                v1[i + 1] = best0 - nc1[i + 1]
                while (dq0.isNotEmpty() && v0[dq0.last() + 1] >= v0[i + 1]) dq0.removeLast()
                dq0.addLast(i)
                while (dq1.isNotEmpty() && v1[dq1.last() + 1] >= v1[i + 1]) dq1.removeLast()
                dq1.addLast(i)
            }
            return minOf(best0, best1)
        }

        var lo = 1
        var hi = n
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (minFlips(mid) <= numOps) hi = mid else lo = mid + 1
        }
        return lo
    }
}
