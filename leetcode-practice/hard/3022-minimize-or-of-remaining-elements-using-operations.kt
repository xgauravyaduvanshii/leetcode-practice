// LeetCode 3022. Minimize OR of Remaining Elements Using Operations — Hard
// https://leetcode.com/problems/minimize-or-of-remaining-elements-using-operations/
// Submission 2201899661 — Accepted, Kotlin
//
// My thinking: I try to switch each bit
// off, from the highest down, keeping a
// bit off only when the array can really
// be merged to avoid it. To test a set of
// allowed bits, I cut the array greedily:
// a piece ends as soon as the AND of its
// numbers uses only allowed bits, since
// AND can only clear bits. Merging the
// pieces takes one operation less than
// the number of numbers, so a test passes
// when the greedy cut leaves few enough
// pieces for the k operations allowed.
// A leftover tail just joins the last
// piece, which costs the same total.

class Solution {
    fun minOrAfterOperations(nums: IntArray, k: Int): Int {
        val n = nums.size
        val all = (1 shl 30) - 1
        var ans = 0
        for (x in nums) ans = ans or x

        fun can(target: Int): Boolean {
            // Can the array be merged (at most k ops) so every
            // remaining number uses only bits set in target?
            var cur = all
            var pieces = 0
            for (x in nums) {
                cur = cur and x
                if (cur and target.inv() == 0) {
                    pieces++
                    cur = all
                }
            }
            // No cut at all means the whole array keeps a bad bit.
            if (pieces == 0) return false
            // Merging into `pieces` pieces costs n - pieces ops
            // (a leftover tail joins the last piece for free in
            // the count, since AND only clears bits).
            return n - pieces <= k
        }

        for (bit in 29 downTo 0) {
            if (ans and (1 shl bit) != 0) {
                if (can(ans and (1 shl bit).inv())) {
                    ans = ans and (1 shl bit).inv()
                }
            }
        }
        return ans
    }
}
