// LeetCode 3241. Time Taken to Mark All Nodes — Hard
// https://leetcode.com/problems/time-taken-to-mark-all-nodes/
// Submission 2202124838 — Accepted, Kotlin
//
// My thinking: moving into a node costs 1 if
// the node is odd and 2 if it is even, so the
// time from a start node is the most expensive
// root-to-leaf walk in any direction. I root
// the tree at 0 and compute down values bottom
// up (best walk inside the subtree) and up
// values top down (best walk outside it, using
// the top two sibling branches), then each
// answer is max(down, up).

class Solution {
    fun timeTaken(edges: Array<IntArray>): IntArray {
        val n = edges.size + 1
        val adj = Array(n) { mutableListOf<Int>() }
        for (e in edges) {
            adj[e[0]].add(e[1])
            adj[e[1]].add(e[0])
        }
        val parent = IntArray(n) { -1 }
        val order = ArrayList<Int>()
        val stack = ArrayDeque<Int>()
        stack.add(0)
        parent[0] = -2
        while (stack.isNotEmpty()) {
            val u = stack.removeLast()
            order.add(u)
            for (v in adj[u]) {
                if (parent[v] == -1) {
                    parent[v] = u
                    stack.add(v)
                }
            }
        }
        val down = IntArray(n)
        for (idx in order.size - 1 downTo 0) {
            val u = order[idx]
            var best = 0
            for (v in adj[u]) {
                if (v == parent[u]) continue
                val cand = (if (v % 2 == 1) 1 else 2) + down[v]
                if (cand > best) best = cand
            }
            down[u] = best
        }
        val up = IntArray(n)
        for (u in order) {
            var top1 = 0
            var top2 = 0
            var cnt1 = 0
            for (v in adj[u]) {
                if (v == parent[u]) continue
                val cand = (if (v % 2 == 1) 1 else 2) + down[v]
                if (cand > top1) {
                    top2 = top1
                    top1 = cand
                    cnt1 = 1
                } else if (cand == top1) {
                    cnt1++
                } else if (cand > top2) {
                    top2 = cand
                }
            }
            val costU = if (u % 2 == 1) 1 else 2
            for (v in adj[u]) {
                if (v == parent[u]) continue
                val cand = (if (v % 2 == 1) 1 else 2) + down[v]
                val sibling = if (cand < top1 || cnt1 >= 2) top1 else top2
                val bestExcl = maxOf(up[u], sibling)
                up[v] = costU + bestExcl
            }
        }
        return IntArray(n) { i -> maxOf(down[i], up[i]) }
    }
}
