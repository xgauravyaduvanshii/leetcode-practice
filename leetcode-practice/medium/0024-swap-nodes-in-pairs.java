// LeetCode 24. Swap Nodes in Pairs — Medium
// https://leetcode.com/problems/swap-nodes-in-pairs/
// Submission 2203811983 — Accepted, Java

// My thinking: I walk the list two nodes at a time with a dummy node
// in front, so the head swap needs no special case. For each pair I
// point the previous node at the second node, the second node back at
// the first, and the first node at whatever comes after the pair, then
// move on to the next pair.
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
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(0, head);
        ListNode prev = dummy;
        while (prev.next != null && prev.next.next != null) {
            ListNode first = prev.next;
            ListNode second = first.next;
            prev.next = second;
            first.next = second.next;
            second.next = first;
            prev = first;
        }
        return dummy.next;
    }
}
