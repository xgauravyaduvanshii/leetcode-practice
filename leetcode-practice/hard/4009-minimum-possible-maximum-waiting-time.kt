// LeetCode 4009. Minimum Possible Maximum Waiting Time — Hard
// https://leetcode.com/problems/minimum-possible-maximum-waiting-time/
// Submission 2203508776 — Accepted, Kotlin
class Solution {
    fun minMaxWaitingTime(demand: IntArray, fuel: IntArray): Int {
        // My thinking: cars are served in order, and the
        // process stops at the first car neither dispenser
        // can fuel, so serving k cars means serving cars
        // 0..k-1. Track each dispenser by how much fuel it
        // has left and by its lag — how long until it is
        // free, measured from the start time of the last
        // car served. A lag is at most the biggest demand
        // (20), because a dispenser frees at most one
        // demand after the last car that used it started.
        // When car i takes a dispenser, it waits exactly
        // that dispenser's lag, the clock advances by the
        // lag, the other dispenser's lag shrinks by the
        // same amount (floored at 0), and the chosen
        // dispenser's new lag is demand[i]. The fuel left
        // in dispenser 1 follows from the fuel left in
        // dispenser 0 and the demands served so far, so a
        // state is (fuel0 left, lag0, lag1), packed into
        // one key as r0*441 + lag0*21 + lag1. Two histories
        // reaching the same state differ only in the worst
        // wait suffered so far, and the smaller one always
        // wins, so keep the minimum worst wait per state.
        // Layer by layer this gives, for the largest
        // reachable number of served cars, the smallest
        // possible maximum waiting time; if not even car 0
        // can be served, the answer is -1.
        val n = demand.size
        val totalFuel = fuel[0] + fuel[1]
        val inf = Int.MAX_VALUE / 2
        var cur = HashMap<Int, Int>()
        cur[fuel[0] * 441] = 0
        var served = 0
        var used = 0
        for (i in 0 until n) {
            val d = demand[i]
            val nxt = HashMap<Int, Int>()
            for ((key, worst) in cur) {
                val r0 = key / 441
                val lag0 = (key / 21) % 21
                val lag1 = key % 21
                val r1 = totalFuel - used - r0
                if (r0 >= d) {
                    val w = maxOf(worst, lag0)
                    val nk = (r0 - d) * 441 + d * 21 + maxOf(0, lag1 - lag0)
                    if (w < nxt.getOrDefault(nk, inf)) nxt[nk] = w
                }
                if (r1 >= d) {
                    val w = maxOf(worst, lag1)
                    val nk = r0 * 441 + maxOf(0, lag0 - lag1) * 21 + d
                    if (w < nxt.getOrDefault(nk, inf)) nxt[nk] = w
                }
            }
            if (nxt.isEmpty()) break
            cur = nxt
            served = i + 1
            used += d
        }
        if (served == 0) return -1
        return cur.values.minOrNull() ?: -1
    }
}
