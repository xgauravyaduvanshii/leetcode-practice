// LeetCode 3569. Maximize Count of Distinct Primes After Split — Hard
// https://leetcode.com/problems/maximize-count-of-distinct-primes-after-split/
// Submission 2202851841 — Accepted, Kotlin
class Solution {
    fun maximumCount(nums: IntArray, queries: Array<IntArray>): IntArray {
        // My thinking: "distinct prime values" means values that are
        // themselves prime numbers, not prime factors — a 4 counts
        // for nothing. For a split k, every distinct prime value
        // contributes 1 (it is on one side or the other), plus one
        // more when the split falls strictly between its first and
        // last occurrence. So the answer is the number of distinct
        // primes plus the largest number of first-to-last intervals
        // covering any split, which I keep in a lazy segment tree
        // while point updates move the interval ends.
        val limit = 100000
        val isPrime = BooleanArray(limit + 1) { true }
        isPrime[0] = false
        isPrime[1] = false
        var i = 2
        while (i * i <= limit) {
            if (isPrime[i]) {
                var j = i * i
                while (j <= limit) { isPrime[j] = false; j += i }
            }
            i++
        }
        val n = nums.size
        val occ = HashMap<Int, MutableList<Int>>()
        for (idx in nums.indices) {
            val x = nums[idx]
            if (isPrime[x]) occ.getOrPut(x) { mutableListOf() }.add(idx)
        }
        for (pos in occ.values) pos.sort()
        val seg = SegMax(n)
        var distinct = 0
        for ((_, pos) in occ) {
            distinct++
            if (pos.size >= 2) seg.add(pos.first() + 1, pos.last(), 1)
        }
        val ans = IntArray(queries.size)
        for ((qi, q) in queries.withIndex()) {
            val idx = q[0]
            val value = q[1]
            val old = nums[idx]
            if (old != value) {
                if (isPrime[old]) {
                    val pos = occ[old]!!
                    if (pos.size >= 2) seg.add(pos.first() + 1, pos.last(), -1)
                    pos.remove(idx)
                    if (pos.isEmpty()) {
                        occ.remove(old)
                        distinct--
                    } else if (pos.size >= 2) {
                        seg.add(pos.first() + 1, pos.last(), 1)
                    }
                }
                nums[idx] = value
                if (isPrime[value]) {
                    val isNew = !occ.containsKey(value)
                    val pos = occ.getOrPut(value) { mutableListOf() }
                    if (pos.size >= 2) seg.add(pos.first() + 1, pos.last(), -1)
                    val at = pos.binarySearch(idx)
                    pos.add(if (at >= 0) at else -at - 1, idx)
                    if (pos.size >= 2) seg.add(pos.first() + 1, pos.last(), 1)
                    if (isNew) distinct++
                }
            }
            ans[qi] = distinct + seg.queryMax()
        }
        return ans
    }

    private class SegMax(n: Int) {
        private var size = 1
        private val maxv: IntArray
        private val lazy: IntArray
        init {
            while (size < n) size *= 2
            maxv = IntArray(2 * size)
            lazy = IntArray(2 * size)
        }
        private fun push(node: Int) {
            if (lazy[node] != 0) {
                for (ch in intArrayOf(node * 2, node * 2 + 1)) {
                    maxv[ch] += lazy[node]
                    lazy[ch] += lazy[node]
                }
                lazy[node] = 0
            }
        }
        private fun add(node: Int, l: Int, r: Int, ql: Int, qr: Int, v: Int) {
            if (qr < l || r < ql) return
            if (ql <= l && r <= qr) {
                maxv[node] += v
                lazy[node] += v
                return
            }
            push(node)
            val mid = (l + r) / 2
            add(node * 2, l, mid, ql, qr, v)
            add(node * 2 + 1, mid + 1, r, ql, qr, v)
            maxv[node] = maxOf(maxv[node * 2], maxv[node * 2 + 1])
        }
        fun add(l: Int, r: Int, v: Int) {
            if (l > r) return
            add(1, 0, size - 1, l, r, v)
        }
        fun queryMax(): Int = maxv[1]
    }
}
