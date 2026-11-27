// LeetCode 1970. Last Day Where You Can Still Cross — Hard
// https://leetcode.com/problems/last-day-where-you-can-still-cross/
// Submission 2201278849 — Accepted, Kotlin
//
// My thinking: crossing gets only harder as cells
// flood, so I binary search the last day that still
// works — each check is just a walk from the top
// row to the bottom row over the dry cells.

import java.util.ArrayDeque

class Solution {
    fun latestDayToCross(row: Int, col: Int, cells: Array<IntArray>): Int {
        fun canCross(day: Int): Boolean {
            val grid = Array(row) { BooleanArray(col) }
            for (i in 0 until day) {
                val (r, c) = cells[i]
                grid[r - 1][c - 1] = true
            }
            val q: ArrayDeque<Pair<Int, Int>> = ArrayDeque()
            val seen = Array(row) { BooleanArray(col) }
            for (c in 0 until col) {
                if (!grid[0][c]) {
                    q.add(0 to c)
                    seen[0][c] = true
                }
            }
            while (q.isNotEmpty()) {
                val (r, c) = q.removeFirst()
                if (r == row - 1) return true
                for ((dr, dc) in listOf(1 to 0, -1 to 0, 0 to 1, 0 to -1)) {
                    val nr = r + dr
                    val nc = c + dc
                    if (nr in 0 until row && nc in 0 until col && !seen[nr][nc] && !grid[nr][nc]) {
                        seen[nr][nc] = true
                        q.add(nr to nc)
                    }
                }
            }
            return false
        }
        var lo = 0
        var hi = cells.size
        while (lo < hi) {
            val mid = (lo + hi + 1) / 2
            if (canCross(mid)) lo = mid else hi = mid - 1
        }
        return lo
    }
}
