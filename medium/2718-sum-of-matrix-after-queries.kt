// LeetCode 2718. Sum of Matrix After Queries — Medium
// https://leetcode.com/problems/sum-of-matrix-after-queries/
// Submission 2205211537 — Accepted, Kotlin
//
// My thinking: same idea as the Python version — replay the
// queries backwards, counting each row or column only on its
// first (i.e. latest) appearance, over the cells the opposite
// side has not already claimed.
class Solution {
    fun matrixSumQueries(n: Int, queries: Array<IntArray>): Long {
        val rows = HashSet<Int>()
        val cols = HashSet<Int>()
        var ans = 0L
        for (i in queries.indices.reversed()) {
            val typ = queries[i][0]
            val idx = queries[i][1]
            val value = queries[i][2].toLong()
            if (typ == 0) {
                if (rows.add(idx)) ans += value * (n - cols.size)
            } else {
                if (cols.add(idx)) ans += value * (n - rows.size)
            }
        }
        return ans
    }
}
