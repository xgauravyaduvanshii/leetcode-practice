// LeetCode 86. Partition List — Medium
// https://leetcode.com/problems/partition-list/
// Submission 2203964117 — Accepted, C#

// My thinking: I walk the list once and split it into two chains —
// one for nodes smaller than x, one for nodes x or larger — keeping
// each node's original relative order inside its own chain, because
// I only ever append to the tail of the chain it belongs to. When the
// walk is done I join the small chain to the head of the large chain
// and cap the large chain's tail with null, so the last large node
// cannot still point back into the small chain and form a cycle.
public class Solution {
    public ListNode Partition(ListNode head, int x) {
        var beforeHead = new ListNode(0);
        var afterHead = new ListNode(0);
        var before = beforeHead;
        var after = afterHead;
        var node = head;
        while (node != null) {
            if (node.val < x) {
                before.next = node;
                before = before.next;
            } else {
                after.next = node;
                after = after.next;
            }
            node = node.next;
        }
        after.next = null;
        before.next = afterHead.next;
        return beforeHead.next;
    }
}
