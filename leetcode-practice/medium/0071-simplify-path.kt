// LeetCode 71. Simplify Path — Medium
// https://leetcode.com/problems/simplify-path/
// Submission 2203843054 — Accepted, Kotlin

// My thinking: I split the path on slashes and walk the parts with a
// stack. A normal name goes on the stack, ".." pops the last directory
// if there is one, and "." and empty parts are ignored. Joining the
// stack with slashes and putting one slash in front gives the clean
// canonical path.
class Solution {
    fun simplifyPath(path: String): String {
        val stack = ArrayDeque<String>()
        for (part in path.split('/')) {
            when (part) {
                "", "." -> {}
                ".." -> if (stack.isNotEmpty()) stack.removeLast()
                else -> stack.addLast(part)
            }
        }
        return "/" + stack.joinToString("/")
    }
}
