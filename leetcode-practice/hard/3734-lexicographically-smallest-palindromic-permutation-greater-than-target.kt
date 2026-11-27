// LeetCode 3734. Lexicographically Smallest Palindromic Permutation Greater Than Target — Hard
// https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/
// Submission 2203138327 — Accepted, Kotlin
class Solution {
    fun lexPalindromicPermutation(s: String, target: String): String {
        // My thinking: a palindrome is fixed by its first half
        // plus at most one odd middle character, so more than one
        // odd frequency means no palindrome exists at all. The
        // smallest palindrome above target either matches target's
        // first half exactly (then the mirror decides whether it
        // is greater), or it matches target's first half up to
        // some position, puts the smallest bigger character there,
        // and fills the rest with the smallest characters left.
        // Trying the exact match first, then the split positions
        // from right to left, gives the smallest answer, since a
        // later split keeps a longer prefix of target.
        val n = s.length
        val freq = IntArray(26)
        for (c in s) freq[c - 'a']++
        var odd = 0
        var middle = ""
        for (i in 0 until 26) {
            if (freq[i] % 2 == 1) {
                odd++
                middle = ('a' + i).toString()
            }
        }
        if (odd > 1) return ""
        val half = IntArray(26) { freq[it] / 2 }
        val halfLen = n / 2
        val targetHalf = target.substring(0, halfLen)

        fun build(left: String): String {
            val right = left.reversed()
            return if (n % 2 == 1) left + middle + right else left + right
        }

        // Exact case: the first half equals target's first half.
        val rem0 = half.copyOf()
        var matched = true
        for (i in 0 until halfLen) {
            val x = targetHalf[i] - 'a'
            if (rem0[x] == 0) {
                matched = false
                break
            }
            rem0[x]--
        }
        if (matched) {
            val cand = build(targetHalf)
            if (cand > target) return cand
        }
        // Split cases: match target's first half up to pos, then
        // raise the character at pos and take the smallest rest.
        for (pos in halfLen - 1 downTo 0) {
            val rem = half.copyOf()
            var ok = true
            for (i in 0 until pos) {
                val x = targetHalf[i] - 'a'
                if (rem[x] == 0) {
                    ok = false
                    break
                }
                rem[x]--
            }
            if (!ok) continue
            val targetChar = targetHalf[pos] - 'a'
            for (c in targetChar + 1 until 26) {
                if (rem[c] > 0) {
                    val sb = StringBuilder()
                    sb.append(targetHalf.substring(0, pos))
                    sb.append('a' + c)
                    rem[c]--
                    for (x in 0 until 26) repeat(rem[x]) { sb.append('a' + x) }
                    val cand = build(sb.toString())
                    if (cand > target) return cand
                    break
                }
            }
        }
        return ""
    }
}
