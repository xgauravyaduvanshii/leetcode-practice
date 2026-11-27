// LeetCode 2410. Maximum Matching of Players With Trainers — Medium
// https://leetcode.com/problems/maximum-matching-of-players-with-trainers/
// Submission 2204791259 — Accepted, Kotlin
//
// My thinking: same idea as the Python version — sort both arrays and
// greedily match the weakest unmatched player with the weakest trainer
// who can handle them.
class Solution {
    fun matchPlayersAndTrainers(players: IntArray, trainers: IntArray): Int {
        players.sort()
        trainers.sort()
        var i = 0
        var ans = 0
        for (t in trainers) {
            if (i < players.size && players[i] <= t) {
                ans++
                i++
            }
        }
        return ans
    }
}
