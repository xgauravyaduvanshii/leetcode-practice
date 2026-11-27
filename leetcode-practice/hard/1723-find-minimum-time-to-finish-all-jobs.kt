// LeetCode 1723. Find Minimum Time to Finish All Jobs — Hard
// https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/
// Submission 2201119061 — Accepted, Kotlin
//
// My thinking: I sort the jobs biggest first and try
// them onto the workers one by one, always pruning a
// branch the moment its busiest worker is no better
// than the best answer I already have — and I skip
// trying a job on an empty worker twice.

class Solution {
    fun minimumTimeRequired(jobs: IntArray, k: Int): Int {
        val sorted = jobs.sortedDescending()
        val workers = IntArray(k)
        var best = sorted.sum()
        fun dfs(i: Int) {
            if (i == sorted.size) {
                best = minOf(best, workers.max())
                return
            }
            val seen = HashSet<Int>()
            for (w in 0 until k) {
                if (workers[w] in seen) continue
                seen.add(workers[w])
                if (workers[w] + sorted[i] >= best) continue
                workers[w] += sorted[i]
                dfs(i + 1)
                workers[w] -= sorted[i]
                if (workers[w] == 0) break
            }
        }
        dfs(0)
        return best
    }
}
