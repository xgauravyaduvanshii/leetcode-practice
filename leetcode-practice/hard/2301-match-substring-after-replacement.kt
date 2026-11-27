// LeetCode 2301. Match Substring After Replacement — Hard
// https://leetcode.com/problems/match-substring-after-replacement/
// Submission 2201666203 — Accepted, Kotlin
//
// My thinking: a replacement only ever
// turns one letter into another, so I try
// every starting spot and check letter by
// letter whether each one already matches
// or is allowed to become the one it faces.

class Solution {
    fun matchReplacement(s: String, sub: String, mappings: Array<CharArray>): Boolean {
        val allowed = mutableMapOf<Char, MutableSet<Char>>()
        for ((old, new) in mappings) {
            allowed.getOrPut(old) { mutableSetOf() }.add(new)
        }
        val n = s.length
        val m = sub.length
        for (i in 0..n - m) {
            var ok = true
            for (j in 0 until m) {
                if (sub[j] == s[i + j]) continue
                if (s[i + j] in (allowed[sub[j]] ?: emptySet())) continue
                ok = false
                break
            }
            if (ok) return true
        }
        return false
    }
}
