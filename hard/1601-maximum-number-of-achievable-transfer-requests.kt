class Solution {
    fun maximumRequests(n: Int, requests: Array<IntArray>): Int {
        // My thinking: a set of moves works when every building
        // sends as many people as it receives — so try the
        // biggest sets first and keep the first one that balances.
        val m = requests.size
        var best = 0
        for (mask in 0 until (1 shl m)) {
            val cnt = Integer.bitCount(mask)
            if (cnt <= best) continue
            val bal = IntArray(n)
            for (i in 0 until m) {
                if (mask shr i and 1 == 1) {
                    bal[requests[i][0]]--
                    bal[requests[i][1]]++
                }
            }
            if (bal.all { it == 0 }) best = cnt
        }
        return best
    }
}
