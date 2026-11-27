// LeetCode 98. Validate Binary Search Tree — Medium
// https://leetcode.com/problems/validate-binary-search-tree/
// Submission 2203976569 — Accepted, JavaScript

// My thinking: a tree is a valid binary search tree only when every
// node sits strictly between the limits handed down from its
// ancestors, not just next to its own parent. So I walk the tree
// carrying a low and a high bound: a node must be greater than low
// and less than high, then its left child inherits the same low with
// the node's value as its new high, and its right child inherits the
// node's value as its new low with the same high. An empty subtree is
// always valid, and if any node breaks its bounds the whole tree is
// invalid.
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function(root) {
    function check(node, low, high) {
        if (node === null) return true;
        if (!(low < node.val && node.val < high)) return false;
        return check(node.left, low, node.val) &&
               check(node.right, node.val, high);
    }
    return check(root, -Infinity, Infinity);
};
