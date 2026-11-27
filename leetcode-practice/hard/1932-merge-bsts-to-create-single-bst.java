// LeetCode 1932. Merge BSTs to Create Single BST — Hard
// https://leetcode.com/problems/merge-bsts-to-create-single-bst/
// Submission 2201249206 — Accepted, Java
//
// My thinking: the final root is the one tree whose
// root is no other tree's leaf — I graft each other
// tree onto the leaf that carries its root value,
// checking the binary-search bounds as I go, and
// the merge only counts when every tree is used.

import java.util.*;

class Solution {
    private Map<Integer, TreeNode> roots;
    private int merged;

    public TreeNode canMerge(List<TreeNode> trees) {
        roots = new HashMap<>();
        List<Set<Integer>> leaves = new ArrayList<>();
        for (TreeNode t : trees) {
            leaves.add(new HashSet<>());
        }
        for (int i = 0; i < trees.size(); i++) {
            TreeNode t = trees.get(i);
            roots.put(t.val, t);
            Deque<TreeNode> stack = new ArrayDeque<>();
            stack.push(t);
            while (!stack.isEmpty()) {
                TreeNode node = stack.pop();
                if (node.left == null && node.right == null) {
                    leaves.get(i).add(node.val);
                }
                if (node.left != null) stack.push(node.left);
                if (node.right != null) stack.push(node.right);
            }
        }
        TreeNode fin = null;
        for (int i = 0; i < trees.size(); i++) {
            TreeNode t = trees.get(i);
            boolean isLeafElsewhere = false;
            for (int j = 0; j < trees.size(); j++) {
                if (j != i && leaves.get(j).contains(t.val)) {
                    isLeafElsewhere = true;
                    break;
                }
            }
            if (!isLeafElsewhere) {
                if (fin != null) return null;
                fin = t;
            }
        }
        if (fin == null) return null;
        merged = 0;
        if (!dfs(fin, Long.MIN_VALUE, Long.MAX_VALUE)) return null;
        if (merged != trees.size() - 1) return null;
        return fin;
    }

    private boolean dfs(TreeNode node, long lo, long hi) {
        if (node == null) return true;
        if (node.val <= lo || node.val >= hi) return false;
        if (node.left == null && node.right == null) {
            TreeNode sub = roots.get(node.val);
            if (sub != null && sub != node) {
                merged++;
                roots.remove(node.val);
                node.left = sub.left;
                node.right = sub.right;
                return dfs(node.left, lo, node.val) && dfs(node.right, node.val, hi);
            }
            return true;
        }
        return dfs(node.left, lo, node.val) && dfs(node.right, node.val, hi);
    }
}
