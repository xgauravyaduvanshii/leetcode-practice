// LeetCode 143. Reorder List — Medium
// https://leetcode.com/problems/reorder-list/
// Submission 2204046320 — Accepted, Kotlin

// My thinking: I split the list in half with a slow and a fast pointer,
// so the slow pointer ends at the middle. I reverse the second half in
// place, then weave the two halves together one node at a time — first
// half, then reversed second half, and so on — until the second half
// runs out. This reorders the list in place, using only O(1) extra
// memory and one pass for each step.
/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun reorderList(head: ListNode?) {
        if (head?.next == null) return

        // Find the middle of the list.
        var slow: ListNode? = head
        var fast: ListNode? = head
        while (fast?.next != null) {
            slow = slow?.next
            fast = fast.next?.next
        }

        // Reverse the second half.
        var prev: ListNode? = null
        var curr: ListNode? = slow?.next
        slow?.next = null
        while (curr != null) {
            val nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        }

        // Merge the two halves alternately.
        var first: ListNode? = head
        var second: ListNode? = prev
        while (second != null) {
            val tmp1 = first?.next
            val tmp2 = second.next
            first?.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        }
    }
}
