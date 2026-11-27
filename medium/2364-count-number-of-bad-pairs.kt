// LeetCode 2364. Count Number of Bad Pairs — Medium
// https://leetcode.com/problems/count-number-of-bad-pairs/
// Submission 2204747078 — Accepted, Kotlin
//
// My thinking: same idea as the Python version — a pair is good exactly
// when nums[i] - i == nums[j] - j, so group indices by that key and
// count good pairs, then subtract from all pairs. Longs are used because
// the pair count can exceed 32 bits.
class Solution {
    fun countBadPairs(nums: IntArray): Long {
        val n = nums.size.toLong()
        val freq = HashMap<Int, Long>()
        var good = 0L
        for (i in nums.indices) {
            val key = nums[i] - i
            val c = freq.getOrDefault(key, 0L)
            good += c
            freq[key] = c + 1
        }
        return n * (n - 1) / 2 - good
    }
}
