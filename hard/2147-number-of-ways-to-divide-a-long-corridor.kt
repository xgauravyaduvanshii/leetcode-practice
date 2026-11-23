// LeetCode 2147. Number of Ways to Divide a Long Corridor — Hard
// https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/
// Submission 2201588670 — Accepted, Kotlin
//
// My thinking: every section needs exactly two
// seats, so the dividers are forced to fall
// between the pairs — and between one pair and
// the next, any of the empty gaps will do, so
// the choices multiply.

class Solution {
    fun numberOfWays(corridor: String): Int {
        val mod = 1_000_000_007L
        val seats = corridor.indices.filter { corridor[it] == 'S' }
        if (seats.isEmpty() || seats.size % 2 == 1) return 0
        var ans = 1L
        var i = 1
        while (i < seats.size - 1) {
            ans = ans * (seats[i + 1] - seats[i]) % mod
            i += 2
        }
        return ans.toInt()
    }
}
