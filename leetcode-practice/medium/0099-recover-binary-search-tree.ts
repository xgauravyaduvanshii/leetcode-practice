// LeetCode 99. Recover Binary Search Tree — Medium
// https://leetcode.com/problems/recover-binary-search-tree/
// Submission 2203985772 — Accepted, TypeScript

// My thinking: An inorder walk of a correct binary search tree visits
// the values in increasing order. Exactly two nodes have been swapped,
// so the inorder sequence has one or two places where a value is bigger
// than the next one (a violation). The first node of the first violation
// and the second node of the last violation are the two swapped nodes.
// If there is only one violation, the two nodes next to it are the pair.
// I do a plain recursive inorder walk, remember the previous node, and
// record the first and second misplaced nodes as I go. At the end I swap
// their values back, which fixes the tree without changing its shape.
// The walk visits each node once.

/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function recoverTree(root: TreeNode | null): void {
    let first: TreeNode | null = null;
    let second: TreeNode | null = null;
    let prev: TreeNode | null = null;

    function inorder(node: TreeNode | null): void {
        if (!node) return;
        inorder(node.left);
        if (prev && prev.val > node.val) {
            if (!first) {
                first = prev;
                second = node;
            } else {
                second = node;
            }
        }
        prev = node;
        inorder(node.right);
    }

    inorder(root);
    const tmp = first!.val;
    first!.val = second!.val;
    second!.val = tmp;
}
