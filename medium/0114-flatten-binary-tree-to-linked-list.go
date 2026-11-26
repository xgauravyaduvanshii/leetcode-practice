// LeetCode 114. Flatten Binary Tree to Linked List — Medium
// https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
// Submission 2204002689 — Accepted, Go

// My thinking: the flattened tree must read like a preorder walk of
// the original tree, with every node keeping only a right child. So I
// walk the tree in preorder with an explicit stack: I pop a node, push
// its right child first and then its left child (so the left child is
// popped next), and then I rewire the popped node — its left child
// becomes nil and its right child becomes whatever is on top of the
// stack, which is exactly the next node in preorder. Because each node
// is pushed and popped once, every node ends up linked right after the
// node before it in preorder, and the last node's right child is nil.
// An empty tree needs nothing done, and a single node is already flat.

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func flatten(root *TreeNode) {
    if root == nil {
        return
    }
    stack := []*TreeNode{root}
    for len(stack) > 0 {
        node := stack[len(stack)-1]
        stack = stack[:len(stack)-1]
        if node.Right != nil {
            stack = append(stack, node.Right)
        }
        if node.Left != nil {
            stack = append(stack, node.Left)
        }
        // The next node in preorder is now on top of the stack
        // (or there is no next node).
        node.Left = nil
        if len(stack) > 0 {
            node.Right = stack[len(stack)-1]
        } else {
            node.Right = nil
        }
    }
}
