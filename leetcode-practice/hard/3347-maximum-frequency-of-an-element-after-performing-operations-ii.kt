// LeetCode 3347. Maximum Frequency of an Element After Performing Operations II — Hard
// https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/
// Submission 2202399120 -- Accepted, Kotlin
class Solution {
    fun maxFrequency(nums: IntArray, k: Int, numOperations: Int): Int {
        // My thinking: sort nums. For a target value v, every element in
        // [v-k, v+k] can be turned into v, and elements already equal to v
        // cost no operation, so the frequency is eq(v) + min(numOperations,
        // inrange(v) - eq(v)). The in-range count only changes when v passes
        // nums[i]-k or nums[i]+k, so it is enough to try v = nums[i]-k,
        // nums[i]+k and nums[i] itself; each query is a binary search.
        // Candidates are Longs because v+k can exceed Int range.
        val sorted = nums.map { it.toLong() }.sorted()
        val cands = HashSet<Long>()
        for (v in sorted) {
            cands.add(v - k)
            cands.add(v + k)
            cands.add(v)
        }
        var ans = 0
        for (v in cands) {
            val lo = lowerBound(sorted, v - k)
            val hi = upperBound(sorted, v + k)
            val eq = upperBound(sorted, v) - lowerBound(sorted, v)
            val inrange = hi - lo
            ans = maxOf(ans, eq + minOf(numOperations, inrange - eq))
        }
        return ans
    }

    private fun lowerBound(a: List<Long>, x: Long): Int {
        var l = 0
        var r = a.size
        while (l < r) {
            val m = (l + r) / 2
            if (a[m] < x) l = m + 1 else r = m
        }
        return l
    }

    private fun upperBound(a: List<Long>, x: Long): Int {
        var l = 0
        var r = a.size
        while (l < r) {
            val m = (l + r) / 2
            if (a[m] <= x) l = m + 1 else r = m
        }
        return l
    }
}
