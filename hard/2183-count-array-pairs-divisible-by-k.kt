// LeetCode 2183. Count Array Pairs Divisible by K — Hard
// https://leetcode.com/problems/count-array-pairs-divisible-by-k/
// Submission 2201605023 — Accepted, Kotlin
//
// My thinking: whether two numbers multiply
// to a multiple of k depends only on what
// each shares with k, so I count how many
// numbers share each divisor and pair the
// divisors whose product k divides.

import kotlin.math.abs

class Solution {
    fun countPairs(nums: IntArray, k: Int): Long {
        fun gcd(a: Int, b: Int): Int {
            var x = abs(a)
            var y = abs(b)
            while (y != 0) {
                val t = x % y
                x = y
                y = t
            }
            return x
        }
        val freq = mutableMapOf<Int, Long>()
        for (x in nums) {
            val g = gcd(x, k)
            freq[g] = (freq[g] ?: 0L) + 1L
        }
        val divs = freq.keys.sorted()
        var ans = 0L
        for (i in divs.indices) {
            for (j in i until divs.size) {
                val d1 = divs[i]
                val d2 = divs[j]
                if ((d1.toLong() * d2) % k == 0L) {
                    ans += if (d1 == d2) {
                        freq[d1]!! * (freq[d1]!! - 1) / 2
                    } else {
                        freq[d1]!! * freq[d2]!!
                    }
                }
            }
        }
        return ans
    }
}
