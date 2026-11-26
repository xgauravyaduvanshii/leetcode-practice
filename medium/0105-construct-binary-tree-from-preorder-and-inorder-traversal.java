// LeetCode 105. Construct Binary Tree from Preorder and Inorder Traversal — Medium
// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
// Submission 2203994248 — Accepted, Java

// My thinking: preorder always visits the root first, so the first
// preorder value is the root of the current subtree. Inorder lists that
// root somewhere in the middle: everything to its left belongs to the
// left subtree and everything to its right belongs to the right subtree.
// I keep a map from each value to its position in inorder, so I can find
// the root's split point in O(1) instead of scanning the list each time.
// A single index into preorder walks forward as I build nodes: each
// recursive call takes the next preorder value as its root, then builds
// the left subtree from the inorder slice left of the root and the right
// subtree from the slice right of it. When a slice is empty, that child
// is null. Each node is created exactly once and each inorder lookup is
// O(1), so the whole build is O(n) time and O(n) space for the map plus
// the recursion stack.
import java.util.HashMap;
import java.util.Map;

class Solution {
    private int preorderIndex;
    private Map<Integer, Integer> inorderIndex;

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        inorderIndex = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            inorderIndex.put(inorder[i], i);
        }
        preorderIndex = 0;
        return build(preorder, 0, inorder.length - 1);
    }

    private TreeNode build(int[] preorder, int left, int right) {
        if (left > right) {
            return null;
        }
        int rootVal = preorder[preorderIndex++];
        TreeNode root = new TreeNode(rootVal);
        int mid = inorderIndex.get(rootVal);
        root.left = build(preorder, left, mid - 1);
        root.right = build(preorder, mid + 1, right);
        return root;
    }
}
