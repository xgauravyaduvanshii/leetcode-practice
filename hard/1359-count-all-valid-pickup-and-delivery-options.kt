class Solution {
    fun countOrders(n: Int): Int {
        // My thinking: with i orders placed, the next pickup
        // can go in any of 2i+1 gaps and its delivery in any
        // of the i+1 gaps after it — multiply it out.
        val MOD = 1_000_000_007L
        var total = 1L
        for (i in 1..n) {
            total = total * i * (2 * i - 1) % MOD
        }
        return total.toInt()
    }
}
