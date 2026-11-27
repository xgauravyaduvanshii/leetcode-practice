// LeetCode 113. Path Sum II — Medium
// https://leetcode.com/problems/path-sum-ii/
// Submission 2203996530 — Accepted, C++

// My thinking: I walk the tree from the root down, carrying the path
// so far and the amount of the target sum still left to reach. At each
// node I subtract its value from the remaining sum and add the node to
// the current path. A path only counts when it ends at a leaf (a node
// with no children) and the remaining sum is exactly zero at that leaf.
// If the node is a leaf and the sum is not zero, this path is a dead
// end, so I drop it. Otherwise I keep going into both children, then
// remove the node from the path before returning (backtracking) so the
// other branches reuse the same path list. This visits every
// root-to-leaf path once, in O(n) time.

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<vector<int>> result;
        vector<int> path;
        dfs(root, targetSum, path, result);
        return result;
    }

private:
    void dfs(TreeNode* node, int remaining, vector<int>& path,
             vector<vector<int>>& result) {
        if (node == nullptr) {
            return;
        }
        path.push_back(node->val);
        remaining -= node->val;
        if (node->left == nullptr && node->right == nullptr) {
            if (remaining == 0) {
                result.push_back(path);
            }
        } else {
            dfs(node->left, remaining, path, result);
            dfs(node->right, remaining, path, result);
        }
        path.pop_back();
    }
};
