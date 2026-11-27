class Solution {
    fun minimumIncompatibility(nums: IntArray, k: Int): Int {
        // My thinking: with at most 16 numbers, list every
        // legal group once — no repeats inside, all the same
        // size — then build the answer group by group over
        // the bitmasks.
        val n = nums.size
        val size = n / k
        val INF = Int.MAX_VALUE / 2
        val cost = HashMap<Int, Int>()
        for (mask in 0 until (1 shl n)) {
            if (Integer.bitCount(mask) != size) continue
            val vals = (0 until n).filter { mask shr it and 1 == 1 }.map { nums[it] }
            if (vals.toSet().size != size) continue
            cost[mask] = vals.max() - vals.min()
        }
        val dp = IntArray(1 shl n) { INF }
        dp[0] = 0
        for (mask in 0 until (1 shl n)) {
            if (dp[mask] == INF) continue
            var first = -1
            for (i in 0 until n) if (mask shr i and 1 == 0) { first = i; break }
            if (first == -1) continue
            for ((sub, c) in cost) {
                if (sub and mask != 0) continue
                if (sub shr first and 1 == 0) continue
                dp[mask or sub] = minOf(dp[mask or sub], dp[mask] + c)
            }
        }
        val ans = dp[(1 shl n) - 1]
        return if (ans == INF) -1 else ans
    }
}
