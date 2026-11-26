// LeetCode 1985. Find the Kth Largest Integer in the Array — Medium
// https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/
// Submission 2204096188 — Accepted, Kotlin

// My thinking: the numbers arrive as strings, so I cannot compare them
// as plain text — "10" would wrongly beat "9". A number with more digits
// is always bigger (there are no leading zeros, except "0" itself), and
// among same-length numbers plain lexicographic order is correct. So I
// sort the strings by (length, value) and take the k-th from the end.
class Solution {
    fun kthLargestNumber(nums: Array<String>, k: Int): String {
        val sorted = nums.sortedWith(compareBy<String>({ it.length }, { it }))
        return sorted[sorted.size - k]
    }
}
