// LeetCode 4119. Minimum Set Bits in a Valid Integer — Hard
// https://leetcode.com/problems/minimum-set-bits-in-a-valid-integer/
// Submission 2203744794 — Accepted, Kotlin

class Solution {
    fun minSetBits(nums: IntArray, k: Int): Int {
        // My thinking: a window's AND has a bit set
        // exactly when that bit appears in all k
        // numbers of the window, so keep a per-bit
        // count over the sliding window (nums[i] <=
        // 10^5 < 2^17, so bits 0..16 are enough) and
        // maintain the window AND mask: a bit joins
        // the mask when its count reaches k and leaves
        // when it drops below k. If any window AND is
        // 0, no y can hit it, so return -1. Otherwise
        // collect the set of window ANDs; a candidate
        // y is valid exactly when no window AND is a
        // submask of FULL ^ y, i.e. y shares a bit
        // with every window AND. Run a SOS DP over
        // the 2^17 masks to mark every submask of
        // each window AND, then scan all y and keep
        // the smallest popcount among the valid ones.
        val n = nums.size
        val cnt = IntArray(17)
        var mask = 0
        val bad = BooleanArray(1 shl 17)
        for (i in 0 until n) {
            var x = nums[i]
            while (x != 0) {
                val lb = x and -x
                val b = Integer.numberOfTrailingZeros(lb)
                cnt[b]++
                if (cnt[b] == k) mask = mask or lb
                x = x xor lb
            }
            if (i >= k) {
                var y = nums[i - k]
                while (y != 0) {
                    val lb = y and -y
                    val b = Integer.numberOfTrailingZeros(lb)
                    if (cnt[b] == k) mask = mask and lb.inv()
                    cnt[b]--
                    y = y xor lb
                }
            }
            if (i >= k - 1) {
                if (mask == 0) return -1
                bad[mask] = true
            }
        }
        val FULL = (1 shl 17) - 1
        for (b in 0 until 17) {
            val step = 1 shl b
            for (m in 0 until (1 shl 17)) {
                if ((m and step) != 0) {
                    bad[m] = bad[m] || bad[m xor step]
                }
            }
        }
        var best = 18
        for (y in 0 until (1 shl 17)) {
            if (!bad[FULL xor y]) {
                val c = Integer.bitCount(y)
                if (c < best) {
                    best = c
                    if (best == 1) break
                }
            }
        }
        return if (best <= 17) best else -1
    }
}
