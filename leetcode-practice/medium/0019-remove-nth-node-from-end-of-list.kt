// LeetCode 19. Remove Nth Node From End of List — Medium
// https://leetcode.com/problems/remove-nth-node-from-end-of-list/
// Submission 2203809835 — Accepted, Kotlin

// My thinking: I put a dummy node in front of the list so removing
// the head is no special case. I send a fast pointer n+1 steps ahead,
// then walk both pointers together until the fast one reaches the end;
// the slow pointer then sits just before the node to remove, and one
// link change drops it out.
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
    fun removeNthFromEnd(head: ListNode?, n: Int): ListNode? {
        val dummy = ListNode(0)
        dummy.next = head
        var fast: ListNode? = dummy
        repeat(n + 1) { fast = fast?.next }
        var slow: ListNode? = dummy
        while (fast != null) {
            fast = fast.next
            slow = slow?.next
        }
        slow?.next = slow?.next?.next
        return dummy.next
    }
}
