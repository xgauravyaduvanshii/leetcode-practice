// LeetCode 2440. Create Components With Same Value — Hard
// https://leetcode.com/problems/create-components-with-same-value/
// Submission 2201743335 — Accepted, Kotlin
//
// My thinking: every piece must add up to
// the same total, so that total has to
// divide the whole sum — I try the
// smallest divisors first, and for each
// one I cut off every subtree that already
// adds up to it, keeping the cut that
// makes the most pieces.

class Solution {
    fun componentValue(nums: IntArray, edges: Array<IntArray>): Int {
        val n = nums.size
        val adj = Array(n) { mutableListOf<Int>() }
        for ((a, b) in edges) {
            adj[a].add(b)
            adj[b].add(a)
        }
        val total = nums.sum()
        fun can(target: Int): Int {
            var count = 0
            fun dfs(u: Int, parent: Int): Int {
                var s = nums[u]
                for (w in adj[u]) {
                    if (w == parent) continue
                    val sub = dfs(w, u)
                    if (sub == -1) return -1
                    s += sub
                }
                if (s == target) {
                    count++
                    return 0
                }
                if (s > target) return -1
                return s
            }
            if (dfs(0, -1) != 0) return -1
            return count - 1
        }
        val divisors = (1..total).filter { total % it == 0 }
        for (target in divisors) {
            val res = can(target)
            if (res != -1) return res
        }
        return 0
    }
}
