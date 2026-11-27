// LeetCode 2056. Number of Valid Move Combinations On Chessboard — Hard
// https://leetcode.com/problems/number-of-valid-move-combinations-on-chessboard/
// Submission 2201563495 — Accepted, Kotlin
//
// My thinking: I list every move each piece can
// make, then try the pieces one by one — a move
// only counts if no two pieces ever share a
// square at the same moment or swap places.

class Solution {
    fun countCombinations(pieces: Array<String>, positions: Array<IntArray>): Int {
        val dirs = mapOf(
            "rook" to listOf(1 to 0, -1 to 0, 0 to 1, 0 to -1),
            "bishop" to listOf(1 to 1, 1 to -1, -1 to 1, -1 to -1),
            "queen" to listOf(1 to 0, -1 to 0, 0 to 1, 0 to -1, 1 to 1, 1 to -1, -1 to 1, -1 to -1)
        )
        val moves = mutableListOf<List<List<Pair<Int, Int>>>>()
        for ((piece, pos) in pieces.zip(positions)) {
            val (r, c) = pos[0] to pos[1]
            val opts = mutableListOf(listOf(r to c))
            for ((dr, dc) in dirs[piece]!!) {
                var nr = r
                var nc = c
                val path = mutableListOf(r to c)
                while (true) {
                    nr += dr
                    nc += dc
                    if (nr !in 1..8 || nc !in 1..8) break
                    path.add(nr to nc)
                    opts.add(path.toList())
                }
            }
            moves.add(opts)
        }
        val n = pieces.size
        val chosen = arrayOfNulls<List<Pair<Int, Int>>>(n)
        var count = 0

        fun at(path: List<Pair<Int, Int>>, t: Int): Pair<Int, Int> =
            if (t < path.size) path[t] else path.last()

        fun conflicts(p: List<Pair<Int, Int>>, q: List<Pair<Int, Int>>): Boolean {
            val m = maxOf(p.size, q.size)
            for (t in 0 until m) {
                if (at(p, t) == at(q, t)) return true
                if (t + 1 < m && at(p, t) == at(q, t + 1) && at(p, t + 1) == at(q, t)) return true
            }
            return false
        }

        fun dfs(i: Int) {
            if (i == n) {
                count++
                return
            }
            for (opt in moves[i]) {
                var ok = true
                for (j in 0 until i) {
                    if (conflicts(opt, chosen[j]!!)) {
                        ok = false
                        break
                    }
                }
                if (ok) {
                    chosen[i] = opt
                    dfs(i + 1)
                    chosen[i] = null
                }
            }
        }

        dfs(0)
        return count
    }
}
