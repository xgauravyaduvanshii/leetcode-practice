// LeetCode 2366. Minimum Replacements to Sort the Array — Hard
// https://leetcode.com/problems/minimum-replacements-to-sort-the-array/
// Submission 2201700842 — Accepted, Kotlin
//
// My thinking: I work from the right,
// where the array must already be sorted —
// a number too big for its neighbour gets
// split into as few even pieces as fit,
// and the smallest piece sets the bar for
// the number before it.

class Solution {
    fun minimumReplacement(nums: IntArray): Long {
        var ops = 0L
        var limit = nums.last().toLong()
        for (i in nums.size - 2 downTo 0) {
            val x = nums[i].toLong()
            if (x <= limit) {
                limit = x
            } else {
                val parts = (x + limit - 1) / limit
                ops += parts - 1
                limit = x / parts
            }
        }
        return ops
    }
}
