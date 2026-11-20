class Solution {
    fun findGoodStrings(n: Int, s1: String, s2: String, evil: String): Int {
        // My thinking: walk the string left to right, staying
        // between the two bounds and tracking how much of the
        // forbidden word we have matched so far — the prefix
        // function tells us where to fall back when a letter
        // breaks the match.
        val MOD = 1_000_000_007
        val m = evil.length
        val pi = IntArray(m)
        for (i in 1 until m) {
            var j = pi[i - 1]
            while (j > 0 && evil[i] != evil[j]) j = pi[j - 1]
            if (evil[i] == evil[j]) j++
            pi[i] = j
        }
        fun nxt(state: Int, ch: Char): Int {
            var s = state
            while (s > 0 && evil[s] != ch) s = pi[s - 1]
            if (evil[s] == ch) s++
            return s
        }
        val memo = HashMap<String, Int>()
        fun dp(pos: Int, lowTight: Boolean, highTight: Boolean, state: Int): Int {
            if (state == m) return 0
            if (pos == n) return 1
            val key = "$pos|$lowTight|$highTight|$state"
            memo[key]?.let { return it }
            var total = 0
            val lo = if (lowTight) s1[pos] else 'a'
            val hi = if (highTight) s2[pos] else 'z'
            var ch = lo
            while (ch <= hi) {
                total = (total + dp(pos + 1, lowTight && ch == s1[pos], highTight && ch == s2[pos], nxt(state, ch))) % MOD
                ch++
            }
            memo[key] = total
            return total
        }
        return dp(0, true, true, 0)
    }
}
