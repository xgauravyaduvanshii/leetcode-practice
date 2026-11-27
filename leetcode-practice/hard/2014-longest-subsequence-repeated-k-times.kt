// LeetCode 2014. Longest Subsequence Repeated k Times — Hard
// https://leetcode.com/problems/longest-subsequence-repeated-k-times/
// Submission 2201314480 — Accepted, Kotlin
//
// My thinking: a letter can only appear if it
// shows up at least k times, and a prefix only
// counts if the whole thing repeated k times
// still fits — so I walk every prefix that fits
// and keep the longest, then the biggest.

class Solution {
    fun longestSubsequenceRepeatedK(s: String, k: Int): String {
        val n = s.length
        val nxt = Array(n + 1) { IntArray(26) { -1 } }
        for (i in n - 1 downTo 0) {
            nxt[i] = nxt[i + 1].copyOf()
            nxt[i][s[i] - 'a'] = i
        }
        fun can(t: String): Boolean {
            var pos = 0
            repeat(k) {
                for (ch in t) {
                    val idx = nxt[pos][ch - 'a']
                    if (idx == -1) return false
                    pos = idx + 1
                }
            }
            return true
        }
        val cnt = IntArray(26)
        for (ch in s) cnt[ch - 'a']++
        val chars = (25 downTo 0).filter { cnt[it] >= k }.map { ('a' + it) }
        var best = ""
        val maxLen = n / k
        fun dfs(t: String) {
            if (t.length > best.length || (t.length == best.length && t > best)) {
                best = t
            }
            if (t.length == maxLen) return
            for (c in chars) {
                if (can(t + c)) dfs(t + c)
            }
        }
        dfs("")
        return best
    }
}
