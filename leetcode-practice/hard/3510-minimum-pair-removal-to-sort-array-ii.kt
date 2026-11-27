// LeetCode 3510. Minimum Pair Removal to Sort Array II — Hard
// https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/
// Submission 2202770603 — Accepted, Kotlin
import java.util.PriorityQueue

class Solution {
    fun minimumPairRemoval(nums: IntArray): Int {
        // My thinking: the process is forced — always merge the
        // adjacent pair with the smallest sum, leftmost on a tie — so I
        // just simulate it. A doubly linked list holds the live array
        // and a heap holds every adjacent pair by (sum, left index);
        // stale heap entries are skipped by checking that both ends are
        // still alive and still neighbours. I count how many adjacent
        // pairs are out of order and stop as soon as that count hits
        // zero, updating it only around the merged pair.
        val n = nums.size
        if (n <= 1) return 0
        val value = nums.map { it.toLong() }.toLongArray()
        val left = IntArray(n) { it - 1 }
        val right = IntArray(n) { it + 1 }
        right[n - 1] = -1
        val alive = BooleanArray(n) { true }
        var bad = 0
        for (i in 0 until n - 1) if (nums[i] > nums[i + 1]) bad++
        val heap = PriorityQueue<Pair<Long, Int>>(compareBy({ it.first }, { it.second }))
        for (i in 0 until n - 1) heap.add(Pair(value[i] + value[i + 1], i))
        var ops = 0
        fun isDescent(a: Int, b: Int): Boolean {
            return a != -1 && b != -1 && alive[a] && alive[b] && value[a] > value[b]
        }
        while (bad > 0) {
            var i: Int
            var j: Int
            while (true) {
                val (ssum, idx) = heap.poll()
                if (!alive[idx]) continue
                val jj = right[idx]
                if (jj == -1 || !alive[jj]) continue
                if (value[idx] + value[jj] != ssum) continue
                i = idx
                j = jj
                break
            }
            val l = left[i]
            val r = right[j]
            if (isDescent(l, i)) bad--
            if (isDescent(i, j)) bad--
            if (isDescent(j, r)) bad--
            value[i] = value[i] + value[j]
            alive[j] = false
            right[i] = r
            if (r != -1) left[r] = i
            if (isDescent(l, i)) bad++
            if (isDescent(i, r)) bad++
            if (l != -1) heap.add(Pair(value[l] + value[i], l))
            if (r != -1) heap.add(Pair(value[i] + value[r], i))
            ops++
        }
        return ops
    }
}
