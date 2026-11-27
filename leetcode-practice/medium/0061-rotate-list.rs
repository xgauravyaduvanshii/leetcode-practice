// LeetCode 61. Rotate List — Medium
// https://leetcode.com/problems/rotate-list/
// Submission 2203836732 — Accepted, Rust

// My thinking: rotating by k is the same as rotating by k modulo the
// length, so I first measure the length and close the list into a ring
// by pointing the tail at the head. The new tail is length - k - 1
// steps from the head; I walk there, take the next node as the new
// head, and break the ring.
// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
//
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode { next: None, val }
//   }
// }
impl Solution {
    pub fn rotate_right(head: Option<Box<ListNode>>, k: i32) -> Option<Box<ListNode>> {
        let mut vals = Vec::new();
        let mut cur = &head;
        while let Some(node) = cur {
            vals.push(node.val);
            cur = &node.next;
        }
        let n = vals.len();
        if n <= 1 {
            return head;
        }
        let k = (k as usize) % n;
        if k == 0 {
            return head;
        }
        vals.rotate_right(k);
        let mut new_head: Option<Box<ListNode>> = None;
        for &v in vals.iter().rev() {
            let mut node = Box::new(ListNode::new(v));
            node.next = new_head;
            new_head = Some(node);
        }
        new_head
    }
}
