// LeetCode 2503. Maximum Number of Points From Grid Queries — Hard
// https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/
// Submission 2201784902 — Accepted, Kotlin
//
// My thinking: a query can only ever
// reach cells smaller than itself, so I
// sort the queries and grow one frontier
// with a min-heap — each cell is claimed
// the first time the heap's smallest wall
// drops below the query, and the running
// count answers every query in order.

import java.util.PriorityQueue

class Solution {
    fun maxPoints(grid: Array<IntArray>, queries: IntArray): IntArray {
        val m = grid.size
        val n = grid[0].size
        val order = queries.indices.sortedBy { queries[it] }
        val ans = IntArray(queries.size)
        val seen = Array(m) { BooleanArray(n) }
        val heap = PriorityQueue<Triple<Int, Int, Int>>(compareBy { it.first })
        heap.add(Triple(grid[0][0], 0, 0))
        seen[0][0] = true
        var points = 0
        for (qi in order) {
            val q = queries[qi]
            while (heap.isNotEmpty() && heap.peek().first < q) {
                val (_, r, c) = heap.poll()
                points++
                for ((dr, dc) in listOf(1 to 0, -1 to 0, 0 to 1, 0 to -1)) {
                    val nr = r + dr
                    val nc = c + dc
                    if (nr in 0 until m && nc in 0 until n && !seen[nr][nc]) {
                        seen[nr][nc] = true
                        heap.add(Triple(grid[nr][nc], nr, nc))
                    }
                }
            }
            ans[qi] = points
        }
        return ans
    }
}
