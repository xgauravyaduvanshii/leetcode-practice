// LeetCode 2381. Shifting Letters II — Medium
// https://leetcode.com/problems/shifting-letters-ii/
// Submission 2204771506 — Accepted, Kotlin
//
// My thinking: same idea as the Python version — a difference array
// turns the range shifts into a per-position total via a prefix sum,
// applied modulo 26 to each letter (with +26 to keep the remainder
// non-negative).
class Solution {
    fun shiftingLetters(s: String, shifts: Array<IntArray>): String {
        val n = s.length
        val diff = IntArray(n + 1)
        for (shift in shifts) {
            val d = if (shift[2] == 1) 1 else -1
            diff[shift[0]] += d
            diff[shift[1] + 1] -= d
        }
        val res = StringBuilder()
        var cur = 0
        for (i in s.indices) {
            cur += diff[i]
            val c = ((s[i] - 'a' + cur) % 26 + 26) % 26
            res.append('a' + c)
        }
        return res.toString()
    }
}
