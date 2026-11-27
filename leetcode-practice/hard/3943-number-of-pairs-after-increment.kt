// LeetCode 3943. Number of Pairs After Increment — Hard
// https://leetcode.com/problems/number-of-pairs-after-increment/
// Submission 2203442150 — Accepted, Kotlin
class Solution {
    fun numberOfPairs(nums1: IntArray, nums2: IntArray, queries: Array<IntArray>): IntArray {
        // My thinking: nums1 has at most 5 entries, so a type 2
        // query only needs the count of each of a few target
        // values in nums2 — but the range adds keep moving those
        // values. Split nums2 into blocks of about 350: each
        // block keeps a frequency map of its raw values plus a
        // lazy add shared by the whole block, so a range add
        // touches at most two partial blocks (rebuild their
        // maps) and just bumps the lazy tag of the full blocks
        // in between. A type 2 query then reads, for each value
        // in nums1, the block maps at (tot - value - lazy),
        // weighted by how many times that value occurs in
        // nums1 — pairs count per index, not per distinct value.
        // Values are Longs: the range adds can push an element
        // far past the Int range.
        val counts1 = HashMap<Int, Int>()
        for (v in nums1) counts1[v] = (counts1[v] ?: 0) + 1
        val a = LongArray(nums2.size) { nums2[it].toLong() }
        val n = a.size
        val b = 350
        val nb = (n + b - 1) / b
        val lazy = LongArray(nb)
        val freq = Array(nb) { HashMap<Long, Int>() }
        for (blk in 0 until nb) {
            val map = freq[blk]
            for (i in blk * b until minOf((blk + 1) * b, n)) {
                val v = a[i]
                map[v] = (map[v] ?: 0) + 1
            }
        }
        fun push(blk: Int) {
            val lz = lazy[blk]
            if (lz != 0L) {
                for (i in blk * b until minOf((blk + 1) * b, n)) a[i] += lz
                lazy[blk] = 0L
            }
        }
        fun rebuild(blk: Int) {
            val map = freq[blk]
            map.clear()
            for (i in blk * b until minOf((blk + 1) * b, n)) {
                val v = a[i]
                map[v] = (map[v] ?: 0) + 1
            }
        }
        val out = ArrayList<Int>()
        for (q in queries) {
            if (q[0] == 1) {
                val x = q[1]
                val y = q[2]
                val v = q[3].toLong()
                val bl = x / b
                val br = y / b
                if (bl == br) {
                    push(bl)
                    for (i in x..y) a[i] += v
                    rebuild(bl)
                } else {
                    push(bl)
                    for (i in x until (bl + 1) * b) a[i] += v
                    rebuild(bl)
                    push(br)
                    for (i in br * b..y) a[i] += v
                    rebuild(br)
                    for (blk in bl + 1 until br) lazy[blk] += v
                }
            } else {
                val tot = q[1].toLong()
                var total = 0
                for ((value, mult) in counts1) {
                    val need = tot - value.toLong()
                    for (blk in 0 until nb) {
                        total += mult * (freq[blk][need - lazy[blk]] ?: 0)
                    }
                }
                out.add(total)
            }
        }
        return out.toIntArray()
    }
}
