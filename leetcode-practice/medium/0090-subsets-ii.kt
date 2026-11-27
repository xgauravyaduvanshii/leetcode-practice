// LeetCode 90. Subsets II — Medium
// https://leetcode.com/problems/subsets-ii/
// Submission 2203966596 — Accepted, Kotlin

// My thinking: this is Subsets with duplicates in the input, so I
// sort the numbers first to bring equal values together. Then I build
// subsets with backtracking, recording the current selection at every
// step. The dedupe rule is: at each level, when a number equals the
// previous one and that previous one was not chosen at this level, I
// skip it — choosing it again would only repeat subsets that were
// already built starting from the earlier equal number.
//
// My thinking: sorting makes duplicates adjacent, which is what makes
// the skip rule work. Backtracking with a start index guarantees each
// subset is built in increasing index order, so no subset is produced
// twice by a different ordering.
class Solution {
    fun subsetsWithDup(nums: IntArray): List<List<Int>> {
        nums.sort()
        val ans = mutableListOf<List<Int>>()
        val current = mutableListOf<Int>()

        fun backtrack(start: Int) {
            ans.add(current.toList())
            for (i in start until nums.size) {
                if (i > start && nums[i] == nums[i - 1]) continue
                current.add(nums[i])
                backtrack(i + 1)
                current.removeAt(current.size - 1)
            }
        }

        backtrack(0)
        return ans
    }
}
