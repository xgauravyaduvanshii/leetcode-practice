// LeetCode 3801. Minimum Cost to Merge Sorted Lists — Hard
// https://leetcode.com/problems/minimum-cost-to-merge-sorted-lists/
// Submission 2203186132 — Accepted, Kotlin
class Solution {
    fun minMergeCost(lists: Array<IntArray>): Long {
        // My thinking: merging two lists costs their total
        // length plus the gap between their medians, and the
        // merged list depends only on which original lists went
        // into it, not on the merge order — so the whole problem
        // is a DP over subsets. For every nonempty subset I
        // precompute its size and its left median (the
        // ((size + 1) / 2)-th smallest value, found by binary
        // searching the sorted distinct values with per-list
        // upper-bound counts). Then f[mask] is the cheapest cost
        // to merge that subset into one list: split it into two
        // nonempty parts, pay their costs plus the median gap,
        // plus the size of the subset itself for the final
        // merge's length part. The answer is f[full mask].
        val n = lists.size
        val vals = lists.flatMap { it.asList() }.toSortedSet().toList()
        val v = vals.size
        // le[i][j] = how many elements of lists[i] are <= vals[j].
        val le = Array(n) { i -> IntArray(v) { j -> upperBound(lists[i], vals[j]) } }
        val full = 1 shl n
        val cnt = IntArray(full)
        for (mask in 1 until full) {
            val lsb = mask and -mask
            val i = Integer.numberOfTrailingZeros(lsb)
            cnt[mask] = cnt[mask xor lsb] + lists[i].size
        }
        val med = IntArray(full)
        for (mask in 1 until full) {
            val need = (cnt[mask] + 1) / 2
            var lo = 0
            var hi = v - 1
            while (lo < hi) {
                val mid = (lo + hi) / 2
                var c = 0
                for (i in 0 until n) {
                    if (mask and (1 shl i) != 0) c += le[i][mid]
                }
                if (c >= need) hi = mid else lo = mid + 1
            }
            med[mask] = vals[lo]
        }
        val INF = Long.MAX_VALUE / 4
        val f = LongArray(full) { INF }
        for (i in 0 until n) f[1 shl i] = 0L
        for (mask in 1 until full) {
            if (mask and (mask - 1) == 0) continue
            var best = INF
            var sub = (mask - 1) and mask
            while (sub != 0) {
                val other = mask xor sub
                if (sub <= other) {
                    val gap = Math.abs(med[sub].toLong() - med[other].toLong())
                    val cand = f[sub] + f[other] + gap
                    if (cand < best) best = cand
                }
                sub = (sub - 1) and mask
            }
            f[mask] = best + cnt[mask]
        }
        return f[full - 1]
    }

    private fun upperBound(list: IntArray, x: Int): Int {
        var lo = 0
        var hi = list.size
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (list[mid] <= x) lo = mid + 1 else hi = mid
        }
        return lo
    }
}
