// LeetCode 148. Sort List — Medium
// https://leetcode.com/problems/sort-list/
// Submission 2204049807 — Accepted, Java

// My thinking: a linked list has no random access, so quicksort-style
// partitioning is awkward, but merge sort fits it perfectly: I split
// the list in half with a slow and fast pointer, sort each half on its
// own, then merge the two sorted halves by walking both and always
// picking the smaller head node. Splitting and merging only rewire
// next pointers, so the sort uses O(log n) extra space for the
// recursion stack and runs in O(n log n) time.

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        // Split the list into two halves with slow/fast pointers.
        ListNode slow = head, fast = head.next;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode mid = slow.next;
        slow.next = null;

        ListNode left = sortList(head);
        ListNode right = sortList(mid);
        return merge(left, right);
    }

    private ListNode merge(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode();
        ListNode tail = dummy;
        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                tail.next = l1;
                l1 = l1.next;
            } else {
                tail.next = l2;
                l2 = l2.next;
            }
            tail = tail.next;
        }
        tail.next = (l1 != null) ? l1 : l2;
        return dummy.next;
    }
}
