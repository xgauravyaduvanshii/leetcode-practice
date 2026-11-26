// LeetCode 47. Permutations II — Medium
// https://leetcode.com/problems/permutations-ii/
// Submission 2203826709 — Accepted, Kotlin

// My thinking: I sort the numbers first so equal values sit together,
// then build permutations with backtracking as in Permutations. The
// extra rule is the dedupe: at each level I skip a number when it
// equals the previous one and that previous one is not currently in
// use, because that arrangement was already covered by the earlier
// equal number.
class Solution {
    fun permuteUnique(nums: IntArray): List<List<Int>> {
        nums.sort()
        val ans = mutableListOf<List<Int>>()
        val current = mutableListOf<Int>()
        val used = BooleanArray(nums.size)

        fun backtrack() {
            if (current.size == nums.size) {
                ans.add(current.toList())
                return
            }
            for (i in nums.indices) {
                if (used[i]) continue
                if (i > 0 && nums[i] == nums[i - 1] && !used[i - 1]) continue
                used[i] = true
                current.add(nums[i])
                backtrack()
                current.removeAt(current.size - 1)
                used[i] = false
            }
        }

        backtrack()
        return ans
    }
}
