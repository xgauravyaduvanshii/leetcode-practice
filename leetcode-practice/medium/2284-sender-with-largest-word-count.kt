// LeetCode 2284. Sender With Largest Word Count — Medium
// https://leetcode.com/problems/sender-with-largest-word-count/
// Submission 2204638275 — Accepted, Kotlin
//
// My thinking: same idea as the Python version — total each sender's
// words, then pick the largest total, breaking ties by the
// lexicographically largest sender name.
class Solution {
    fun largestWordCount(messages: Array<String>, senders: Array<String>): String {
        val counts = mutableMapOf<String, Int>()
        for (i in messages.indices) {
            val words = messages[i].split(" ").filter { it.isNotEmpty() }.size
            counts[senders[i]] = counts.getOrDefault(senders[i], 0) + words
        }
        var best = ""
        var bestCount = -1
        for ((sender, c) in counts) {
            if (c > bestCount || (c == bestCount && sender > best)) {
                best = sender
                bestCount = c
            }
        }
        return best
    }
}
