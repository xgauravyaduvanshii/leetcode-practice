// LeetCode 109. Convert Sorted List to Binary Search Tree — Medium
// https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
// Submission 2203999384 — Accepted, JavaScript

// My thinking: the list is already sorted, so the middle element is
// the natural root of a height-balanced tree — everything smaller
// belongs on the left and everything bigger on the right. I first
// copy the linked list into an array so I can reach the middle of
// any slice in constant time, then build recursively: pick the middle
// value as the root, build the left subtree from the values before
// it and the right subtree from the values after it, and stop when a
// slice is empty. Because each root splits its slice in half, the
// tree comes out height-balanced, and an in-order walk of the tree
// gives back the original sorted list.
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {ListNode} head
 * @return {TreeNode}
 */
var sortedListToBST = function(head) {
    const nums = [];
    let node = head;
    while (node !== null) {
        nums.push(node.val);
        node = node.next;
    }

    function build(lo, hi) {
        if (lo > hi) return null;
        const mid = Math.floor((lo + hi) / 2);
        const root = new TreeNode(nums[mid]);
        root.left = build(lo, mid - 1);
        root.right = build(mid + 1, hi);
        return root;
    }

    return build(0, nums.length - 1);
};
