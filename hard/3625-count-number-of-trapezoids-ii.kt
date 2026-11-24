// LeetCode 3625. Count Number of Trapezoids II — Hard
// https://leetcode.com/problems/count-number-of-trapezoids-ii/
// Submission 2202888443 — Accepted, Kotlin
import kotlin.math.abs

class Solution {
    fun countTrapezoids(points: Array<IntArray>): Int {
        // My thinking: two parallel segments on different lines
        // always form a trapezoid, and segments on different lines
        // with the same slope never share an endpoint. So for each
        // slope I group segments by their line and count the pairs
        // drawn from different lines. A parallelogram is counted
        // once per direction, so I count parallelograms separately
        // — two diagonals with the same midpoint, unless they are
        // collinear — and subtract one copy of each.
        val n = points.size
        fun gcd(a: Int, b: Int): Int {
            var x = abs(a)
            var y = abs(b)
            while (y != 0) {
                val t = x % y
                x = y
                y = t
            }
            return x
        }
        fun norm(dx0: Int, dy0: Int): Pair<Int, Int> {
            var dx = dx0
            var dy = dy0
            val g = gcd(dx, dy)
            dx /= g
            dy /= g
            if (dx < 0 || (dx == 0 && dy < 0)) {
                dx = -dx
                dy = -dy
            }
            return Pair(dx, dy)
        }
        val slopeLines = mutableMapOf<Pair<Int, Int>, MutableMap<Int, Int>>()
        for (i in 0 until n) {
            val (x1, y1) = points[i]
            for (j in i + 1 until n) {
                val (x2, y2) = points[j]
                val (dx, dy) = norm(x2 - x1, y2 - y1)
                val line = dy * x1 - dx * y1
                val lines = slopeLines.getOrPut(Pair(dx, dy)) { mutableMapOf() }
                lines[line] = (lines[line] ?: 0) + 1
            }
        }
        var totalPairs = 0L
        for (lines in slopeLines.values) {
            val total = lines.values.sum()
            totalPairs += total.toLong() * (total - 1) / 2 - lines.values.sumOf { c -> c.toLong() * (c - 1) / 2 }
        }
        val mid = mutableMapOf<Pair<Int, Int>, MutableList<Pair<Int, Int>>>()
        for (i in 0 until n) {
            val (x1, y1) = points[i]
            for (j in i + 1 until n) {
                val (x2, y2) = points[j]
                mid.getOrPut(Pair(x1 + x2, y1 + y2)) { mutableListOf() }.add(Pair(i, j))
            }
        }
        var parallelograms = 0L
        for (pairs in mid.values) {
            val k = pairs.size
            if (k < 2) continue
            val slopes = mutableMapOf<Pair<Int, Int>, Int>()
            for ((i, j) in pairs) {
                val (dx, dy) = norm(points[j][0] - points[i][0], points[j][1] - points[i][1])
                val key = Pair(dx, dy)
                slopes[key] = (slopes[key] ?: 0) + 1
            }
            parallelograms += k.toLong() * (k - 1) / 2 - slopes.values.sumOf { c -> c.toLong() * (c - 1) / 2 }
        }
        return (totalPairs - parallelograms).toInt()
    }
}
