// LeetCode 2310. Sum of Numbers With Units Digit K — Medium
// https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/
// Submission 2204670285 — Accepted, Kotlin
//
// My thinking: same idea as the Python version — with i numbers the
// units digits must sum to i*k, so (num - i*k) % 10 has to be 0; try
// i = 1..10 and return -1 when none works.
class Solution {
    fun minimumNumbers(num: Int, k: Int): Int {
        if (num == 0) return 0
        for (i in 1..10) {
            if (i * k > num) break
            if ((num - i * k) % 10 == 0) return i
        }
        return -1
    }
}
