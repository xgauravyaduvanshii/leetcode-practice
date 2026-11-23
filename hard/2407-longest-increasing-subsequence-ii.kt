// LeetCode 2407. Longest Increasing Subsequence II — Hard
// https://leetcode.com/problems/longest-increasing-subsequence-ii/
// Submission 2201723697 — Accepted, Kotlin
//
// My thinking: each number extends the
// best run ending just below it — I keep
// those best runs in a segment tree and
// ask it for the best run in the window
// [value - k, value - 1] before I extend.

class Solution {
    fun lengthOfLIS(nums: IntArray, k: Int): Int {
        var size = 1
        while (size < (nums.maxOrNull() ?: 0) + 2) size *= 2
        val tree = IntArray(2 * size)
        fun query(lo0: Int, hi0: Int): Int {
            var lo = lo0 + size
            var hi = hi0 + size
            var best = 0
            while (lo <= hi) {
                if (lo % 2 == 1) { best = maxOf(best, tree[lo]); lo++ }
                if (hi % 2 == 0) { best = maxOf(best, tree[hi]); hi-- }
                lo /= 2
                hi /= 2
            }
            return best
        }
        fun update(pos0: Int, value: Int) {
            var pos = pos0 + size
            tree[pos] = maxOf(tree[pos], value)
            pos /= 2
            while (pos > 0) {
                tree[pos] = maxOf(tree[2 * pos], tree[2 * pos + 1])
                pos /= 2
            }
        }
        var ans = 0
        for (x in nums) {
            val lo = maxOf(1, x - k)
            val length = query(lo, x - 1) + 1
            ans = maxOf(ans, length)
            update(x, length)
        }
        return ans
    }
}
