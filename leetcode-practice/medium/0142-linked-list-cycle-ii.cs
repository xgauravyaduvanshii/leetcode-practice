// LeetCode 142. Linked List Cycle II — Medium
// https://leetcode.com/problems/linked-list-cycle-ii/
// Submission 2204043245 — Accepted, C#

// My thinking: I use Floyd's two-pointer trick in two phases. First,
// a slow pointer moving one step and a fast pointer moving two steps
// will meet inside the cycle if there is one — the fast pointer laps
// the slow one, so no meeting means no cycle and I return null. Once
// they meet, I send a second pointer back to the head and walk it and
// the slow pointer one step at a time; they meet exactly at the node
// where the cycle begins, because the distance from the head to the
// cycle start equals the distance from the meeting point around the
// cycle to the start. This needs no extra memory and one pass.
public class Solution {
    public ListNode DetectCycle(ListNode head) {
        var slow = head;
        var fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                var entry = head;
                while (entry != slow) {
                    entry = entry.next;
                    slow = slow.next;
                }
                return entry;
            }
        }
        return null;
    }
}
