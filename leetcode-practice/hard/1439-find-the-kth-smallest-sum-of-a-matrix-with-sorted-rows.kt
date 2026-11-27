import java.util.PriorityQueue

class Solution {
    fun kthSmallest(mat: Array<IntArray>, k: Int): Int {
        // My thinking: the smallest sum takes the first column
        // everywhere — then keep a heap of the next best sums,
        // each one bumping a single row to its next column.
        val rows = mat.size
        val cols = mat[0].size
        val start = IntArray(rows)
        var total = 0
        for (r in 0 until rows) total += mat[r][0]
        val heap = PriorityQueue<Pair<Int, List<Int>>>(compareBy { it.first })
        heap.add(total to start.toList())
        val seen = HashSet<List<Int>>()
        seen.add(start.toList())
        repeat(k - 1) {
            val (sum, idx) = heap.poll()
            for (r in 0 until rows) {
                if (idx[r] + 1 < cols) {
                    val next = idx.toMutableList()
                    next[r] = next[r] + 1
                    if (seen.add(next)) {
                        heap.add((sum - mat[r][idx[r]] + mat[r][idx[r] + 1]) to next)
                    }
                }
            }
        }
        return heap.peek().first
    }
}
