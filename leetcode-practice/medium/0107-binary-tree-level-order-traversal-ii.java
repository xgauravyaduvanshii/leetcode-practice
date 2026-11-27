// LeetCode 107. Binary Tree Level Order Traversal II — Medium
// https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
// Submission 2204101669 — Accepted, Java

// My thinking: this is the same level-by-level walk as ordinary
// level order traversal, only the levels come out bottom-up. So I
// walk the tree breadth-first with a queue, collecting one list of
// values per level from top to bottom, and at the end I reverse the
// list of levels. Each level's children are queued in left-to-right
// order, so the values inside every level stay in the right order,
// and reversing only flips the order of the levels themselves. An
// empty tree gives an empty answer, and a single node gives one
// level containing just that node.
import java.util.*;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        List<List<Integer>> levels = new ArrayList<>();
        if (root == null) {
            return levels;
        }
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            List<Integer> level = new ArrayList<>();
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                level.add(node.val);
                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
            }
            levels.add(level);
        }
        Collections.reverse(levels);
        return levels;
    }
}
