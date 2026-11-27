// LeetCode 102. Binary Tree Level Order Traversal — Medium
// https://leetcode.com/problems/binary-tree-level-order-traversal/
// Submission 2203988934 — Accepted, C#

// My thinking: I walk the tree level by level with a queue,
// starting with just the root. Each pass takes every node
// currently in the queue — that is exactly one level — records
// their values, and queues up their children for the next
// pass. An empty tree has no levels, so it gives back an
// empty list.
public class Solution {
    public IList<IList<int>> LevelOrder(TreeNode root) {
        var result = new List<IList<int>>();
        if (root == null) {
            return result;
        }
        var queue = new Queue<TreeNode>();
        queue.Enqueue(root);
        while (queue.Count > 0) {
            var level = new List<int>();
            int levelSize = queue.Count;
            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.Dequeue();
                level.Add(node.val);
                if (node.left != null) {
                    queue.Enqueue(node.left);
                }
                if (node.right != null) {
                    queue.Enqueue(node.right);
                }
            }
            result.Add(level);
        }
        return result;
    }
}
