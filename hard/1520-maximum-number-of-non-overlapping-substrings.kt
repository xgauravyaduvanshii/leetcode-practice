class Solution {
    fun maxNumOfSubstrings(s: String): List<String> {
        // My thinking: each letter forces its whole span into
        // one piece — so grow every letter's span until it
        // closes, then take the most pieces that don't touch.
        val first = IntArray(26) { -1 }
        val last = IntArray(26) { -1 }
        for (i in s.indices) {
            val c = s[i] - 'a'
            if (first[c] == -1) first[c] = i
            last[c] = i
        }
        val intervals = mutableListOf<Pair<Int, Int>>()
        for (c in 0 until 26) {
            if (first[c] == -1) continue
            var lo = first[c]
            var hi = last[c]
            var j = lo
            while (j <= hi) {
                val d = s[j] - 'a'
                lo = minOf(lo, first[d])
                hi = maxOf(hi, last[d])
                j++
            }
            if (lo == first[c]) intervals.add(hi to lo)
        }
        intervals.sort()
        val out = mutableListOf<String>()
        var prevEnd = -1
        for ((hi, lo) in intervals) {
            if (lo > prevEnd) {
                out.add(s.substring(lo, hi + 1))
                prevEnd = hi
            }
        }
        return out
    }
}
