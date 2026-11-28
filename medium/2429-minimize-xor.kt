// LeetCode 2429. Minimize XOR — Medium
// https://leetcode.com/problems/minimize-xor/
// Submission 2204863705 — Accepted, Kotlin
//
// My thinking: same idea as the Python version — match num1's set
// bits from the highest down first, then fill any remaining bits on
// the lowest unset positions.
class Solution {
    fun minimizeXor(num1: Int, num2: Int): Int {
        var need = Integer.bitCount(num2)
        var x = 0
        for (b in 30 downTo 0) {
            if (need > 0 && ((num1 shr b) and 1) == 1) {
                x = x or (1 shl b)
                need--
            }
        }
        for (b in 0..30) {
            if (need > 0 && ((x shr b) and 1) == 0) {
                x = x or (1 shl b)
                need--
            }
        }
        return x
    }
}
