// LeetCode 95. Unique Binary Search Trees II — Medium
// https://leetcode.com/problems/unique-binary-search-trees-ii/
// Submission 2203979910 — Accepted, Go

// My thinking: in a binary search tree the inorder traversal is sorted,
// so for the values 1..n the root must be some value i, every value
// smaller than i goes in the left subtree and every value larger than i
// goes in the right subtree.
// That splits the problem into two independent smaller problems: build
// all BSTs from the values below i, and all BSTs from the values above
// i. Every left tree pairs with every right tree to make a distinct
// overall tree with i as the root, so we take the cartesian product of
// the two lists.
// The recursion bottoms out when the range is empty: there is exactly
// one empty tree, represented by nil, so a leaf node still gets one
// left and one right combination.
// We repeat this for every possible root i and collect all the trees.
// The count grows like the Catalan numbers, which is why the problem
// only asks for n up to 8.

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func generateTrees(n int) []*TreeNode {
    var build func(lo, hi int) []*TreeNode
    build = func(lo, hi int) []*TreeNode {
        // Empty range: exactly one empty tree.
        if lo > hi {
            return []*TreeNode{nil}
        }
        var trees []*TreeNode
        for rootVal := lo; rootVal <= hi; rootVal++ {
            leftTrees := build(lo, rootVal-1)
            rightTrees := build(rootVal+1, hi)
            for _, left := range leftTrees {
                for _, right := range rightTrees {
                    trees = append(trees, &TreeNode{Val: rootVal, Left: left, Right: right})
                }
            }
        }
        return trees
    }

    return build(1, n)
}
