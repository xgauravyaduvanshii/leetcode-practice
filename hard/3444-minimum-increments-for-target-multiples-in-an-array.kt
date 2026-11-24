// LeetCode 3444. Minimum Increments for Target Multiples in an Array — Hard
// https://leetcode.com/problems/minimum-increments-for-target-multiples-in-an-array/
// Submission 2202539782 — Accepted 590/590, Kotlin
class Solution {
    fun minimumIncrements(nums: IntArray, target: IntArray): Int {
        // My thinking: each target must be covered by some element, and
        // one element can cover several targets at once if it is raised
        // to a multiple of their lcm. So I split the targets into groups,
        // one element per group, and the cheapest element for a group is
        // the cheapest way to reach a multiple of that group's lcm. For
        // each group only its 5 cheapest elements can matter (at most 3
        // other groups can take better ones), so I try every split and
        // every pick of distinct elements from those short lists.
        val m = target.size
        val full = (1 shl m) - 1
        fun gcd(a: Long, b: Long): Long = if (b == 0L) a else gcd(b, a % b)
        // lcm of every nonempty subset of targets
        val subsetLcm = LongArray(1 shl m)
        for (mask in 1 until (1 shl m)) {
            var l = 1L
            for (j in 0 until m) {
                if (mask and (1 shl j) != 0) {
                    val t = target[j].toLong()
                    l = l / gcd(l, t) * t
                }
            }
            subsetLcm[mask] = l
        }
        // 5 cheapest (cost, index) per subset
        val best = Array(1 shl m) { listOf<Pair<Long, Int>>() }
        for (mask in 1 until (1 shl m)) {
            val l = subsetLcm[mask]
            best[mask] = nums.indices.map { i ->
                val x = nums[i].toLong()
                (l - x % l) % l to i
            }.sortedBy { it.first }.take(5)
        }
        // all set partitions of the target set, as lists of masks
        fun partitions(rem: Int): List<List<Int>> {
            if (rem == 0) return listOf(emptyList())
            val low = rem and -rem
            val out = mutableListOf<List<Int>>()
            var sub = rem
            while (sub != 0) {
                if (sub and low != 0) {
                    for (rest in partitions(rem xor sub)) {
                        out.add(listOf(sub) + rest)
                    }
                }
                sub = (sub - 1) and rem
            }
            return out
        }
        var ans = Long.MAX_VALUE
        for (part in partitions(full)) {
            val groups = part.map { best[it] }
            // pick one distinct element per group, cheapest total
            fun rec(gi: Int, used: MutableSet<Int>, total: Long) {
                if (total >= ans) return
                if (gi == groups.size) {
                    ans = total
                    return
                }
                for ((cost, idx) in groups[gi]) {
                    if (idx !in used) {
                        used.add(idx)
                        rec(gi + 1, used, total + cost)
                        used.remove(idx)
                    }
                }
            }
            rec(0, mutableSetOf(), 0L)
        }
        return ans.toInt()
    }
}
