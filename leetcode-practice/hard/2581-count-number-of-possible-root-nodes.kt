// LeetCode 2581. Count Number of Possible Root Nodes — Hard
// https://leetcode.com/problems/count-number-of-possible-root-nodes/
// Submission 2201833357 — Accepted, Kotlin
//
// My thinking: I root the tree once and
// count the guesses that already point
// the right way, then I walk the root
// across each edge — only the guesses on
// that edge can flip, so every other
// root's count follows for free.

class Solution {
    fun rootCount(edges: Array<IntArray>, guesses: Array<IntArray>, k: Int): Int {
        val n = edges.size + 1
        val adj = Array(n) { mutableListOf<Int>() }
        for ((a, b) in edges) {
            adj[a].add(b)
            adj[b].add(a)
        }
        // guesses may repeat: count each occurrence, it counts that many times
        val guessCount = HashMap<Pair<Int, Int>, Int>()
        for ((u, v) in guesses) {
            val key = u to v
            guessCount[key] = (guessCount[key] ?: 0) + 1
        }
        val parent = IntArray(n) { -1 }
        val order = ArrayList<Int>()
        parent[0] = -2
        order.add(0)
        var head = 0
        while (head < order.size) {
            val u = order[head++]
            for (w in adj[u]) {
                if (parent[w] == -1) {
                    parent[w] = u
                    order.add(w)
                }
            }
        }
        val cnt = IntArray(n)
        var c0 = 0
        for ((u, v) in guesses) {
            if (parent[v] == u) c0++
        }
        cnt[0] = c0
        for (u in order) {
            for (w in adj[u]) {
                if (parent[w] == u) {
                    cnt[w] = cnt[u] - (guessCount[u to w] ?: 0) + (guessCount[w to u] ?: 0)
                }
            }
        }
        return cnt.count { it >= k }
    }
}
