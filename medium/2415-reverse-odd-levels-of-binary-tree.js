// LeetCode 2415. Reverse Odd Levels of Binary Tree — Medium
// https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/
// Submission 2204796345 — Accepted, JavaScript
//
// My thinking: same idea as the Python version — BFS level by level;
// on odd levels the values are written back reversed, swapping
// symmetric nodes' values while the structure stays untouched.
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
 * @return {TreeNode}
 */
var reverseOddLevels = function(root) {
    let q = [root];
    let level = 0;
    while (q.length > 0) {
        const n = q.length;
        const nodes = [];
        for (let i = 0; i < n; i++) {
            const node = q.shift();
            nodes.push(node);
            if (node.left) q.push(node.left);
            if (node.right) q.push(node.right);
        }
        if (level % 2 === 1) {
            const vals = nodes.map(node => node.val).reverse();
            for (let i = 0; i < nodes.length; i++) {
                nodes[i].val = vals[i];
            }
        }
        level++;
    }
    return root;
};
