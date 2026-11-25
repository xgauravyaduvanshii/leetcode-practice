// LeetCode 3768. Minimum Inversion Count in Subarrays of Fixed Length — Hard
// https://leetcode.com/problems/minimum-inversion-count-in-subarrays-of-fixed-length/
// Submission 2203169753 — Accepted, Kotlin
class Solution {
    fun minInversionCount(nums: IntArray, k: Int): Long {
        // My thinking: slide a window of length k across nums
        // and keep its inversion count up to date with a
        // Fenwick tree over the compressed values. Dropping the
        // leftmost element x removes exactly the inversions it
        // formed with smaller elements still in the window;
        // adding a new rightmost element y adds exactly the
        // inversions it forms with larger elements already in
        // the window. Both updates are one Fenwick query each,
        // so every window costs O(log n) and the answer is the
        // smallest count seen.
        val ranks = nums.toSortedSet().withIndex().associate { (i, v) -> v to i + 1 }
        val m = ranks.size
        val bit = LongArray(m + 1)
        fun add(i: Int, delta: Long) {
            var j = i
            while (j <= m) {
                bit[j] += delta
                j += j and -j
            }
        }
        fun prefix(i: Int): Long {
            var j = i
            var s = 0L
            while (j > 0) {
                s += bit[j]
                j -= j and -j
            }
            return s
        }
        var inv = 0L
        for (i in 0 until k) {
            val r = ranks.getValue(nums[i])
            inv += i - prefix(r)
            add(r, 1)
        }
        var ans = inv
        for (i in k until nums.size) {
            val rOut = ranks.getValue(nums[i - k])
            inv -= prefix(rOut - 1)
            add(rOut, -1)
            val rIn = ranks.getValue(nums[i])
            inv += (k - 1) - prefix(rIn)
            add(rIn, 1)
            ans = minOf(ans, inv)
        }
        return ans
    }
}
