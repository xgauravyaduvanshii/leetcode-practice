// LeetCode 2012. Sum of Beauty in the Array — Medium
// https://leetcode.com/problems/sum-of-beauty-in-the-array/
// Submission 2204128268 — Accepted, Kotlin

// My thinking: For each middle index i, beauty 2 needs nums[i] to be
// bigger than EVERYTHING before it and smaller than EVERYTHING after
// it, not just its two neighbours. So I precompute, for each i, the
// largest value to its left and the smallest value to its right.
// If max-left < nums[i] < min-right, it scores 2. Otherwise it can
// still score 1 if it is strictly bigger than its left neighbour and
// strictly smaller than its right neighbour. Anything else scores 0.
// One pass each way builds the two helper arrays, then one more pass
// adds up the scores, so the whole thing runs in linear time.
class Solution {
    fun sumOfBeauties(nums: IntArray): Int {
        val n = nums.size

        // maxLeft[i] = largest value among nums[0..i-1]
        val maxLeft = IntArray(n)
        var best = nums[0]
        for (i in 1 until n) {
            maxLeft[i] = best
            best = maxOf(best, nums[i])
        }

        // minRight[i] = smallest value among nums[i+1..n-1]
        val minRight = IntArray(n)
        best = nums[n - 1]
        for (i in n - 2 downTo 0) {
            minRight[i] = best
            best = minOf(best, nums[i])
        }

        var total = 0
        for (i in 1 until n - 1) {
            if (maxLeft[i] < nums[i] && nums[i] < minRight[i]) {
                total += 2
            } else if (nums[i - 1] < nums[i] && nums[i] < nums[i + 1]) {
                total += 1
            }
        }
        return total
    }
}
