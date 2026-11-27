// LeetCode 92. Reverse Linked List II — Medium
// https://leetcode.com/problems/reverse-linked-list-ii/
// Submission 2203974112 — Accepted, C++
//
// My thinking: Only the segment from position left to position
// right needs reversing; everything before left and after right
// stays exactly as it is. I put a dummy node in front of the head
// so the case left == 1 needs no special handling. Then I walk to
// the node just before the segment (call it prev) and take the first
// node of the segment as its tail. From there I reverse the segment
// one link at a time: at each step I lift the node after the tail
// out and plug it in right after prev, so the segment grows reversed
// at the front while the tail stays put. After right - left such
// moves the segment is fully reversed, and I reconnect its tail to
// the untouched remainder of the list.

class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        ListNode dummy(0);
        dummy.next = head;
        ListNode* prev = &dummy;
        for (int i = 1; i < left; i++) {
            prev = prev->next;
        }

        // tail is the first node of the segment; it ends up last after reversal.
        ListNode* tail = prev->next;
        for (int i = 0; i < right - left; i++) {
            ListNode* nxt = tail->next;
            tail->next = nxt->next;
            nxt->next = prev->next;
            prev->next = nxt;
        }
        return dummy.next;
    }
};
