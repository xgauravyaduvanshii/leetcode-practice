// LeetCode 129. Sum Root to Leaf Numbers — Medium
// https://leetcode.com/problems/sum-root-to-leaf-numbers/
// Submission 2204024857 — Accepted, C++
//
// My thinking: Each root-to-leaf path spells out one number, digit
// by digit, so I walk the tree carrying the number built so far. At
// each node I extend it by one digit (multiply by 10 and add the
// node's value). When I reach a leaf, that completed number is one
// of the terms in the answer, so I add it to the total. Inner nodes
// contribute nothing themselves — they only pass their partial number
// down to their children. A depth-first walk visits each node once.

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
    int sumNumbers(TreeNode* root) {
        int total = 0;
        dfs(root, 0, total);
        return total;
    }

private:
    void dfs(TreeNode* node, int num, int& total) {
        if (!node) return;
        num = num * 10 + node->val;
        if (!node->left && !node->right) {
            total += num;
            return;
        }
        dfs(node->left, num, total);
        dfs(node->right, num, total);
    }
};
