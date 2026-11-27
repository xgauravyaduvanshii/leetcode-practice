// LeetCode 2385. Amount of Time for Binary Tree to Be Infected — Medium
// https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/
// Submission 2204779211 — Accepted, C++
//
// My thinking: same idea as the Python version — map each node to its
// parent, then BFS from the start node over left/right/parent; the
// distance of the last node reached is the answer.
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
    int amountOfTime(TreeNode* root, int start) {
        unordered_map<TreeNode*, TreeNode*> parent;
        TreeNode* startNode = nullptr;
        vector<TreeNode*> stack = {root};
        while (!stack.empty()) {
            TreeNode* node = stack.back();
            stack.pop_back();
            if (node->val == start) startNode = node;
            if (node->left) {
                parent[node->left] = node;
                stack.push_back(node->left);
            }
            if (node->right) {
                parent[node->right] = node;
                stack.push_back(node->right);
            }
        }
        unordered_set<TreeNode*> seen;
        seen.insert(startNode);
        queue<pair<TreeNode*, int>> q;
        q.push({startNode, 0});
        int ans = 0;
        while (!q.empty()) {
            auto [node, d] = q.front();
            q.pop();
            ans = d;
            vector<TreeNode*> nbs = {node->left, node->right, parent.count(node) ? parent[node] : nullptr};
            for (TreeNode* nb : nbs) {
                if (nb && !seen.count(nb)) {
                    seen.insert(nb);
                    q.push({nb, d + 1});
                }
            }
        }
        return ans;
    }
};
