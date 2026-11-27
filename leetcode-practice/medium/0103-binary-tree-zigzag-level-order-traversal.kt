// LeetCode 103. Binary Tree Zigzag Level Order Traversal — Medium
// https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
// Submission 2203991256 — Accepted, Kotlin

// My thinking: I walk the tree one level at a time with a queue,
// just like a normal level-order traversal. The only extra step is
// that the direction flips after each level: even levels read
// left to right, odd levels read right to left. Instead of
// reversing the queue (which would break the children's order),
// I collect each level's values and reverse just that level's
// list when the direction is right to left. The children are
// always queued in left-to-right order, so the next level still
// comes out correctly.
class Solution {
    fun zigzagLevelOrder(root: TreeNode?): List<List<Int>> {
        if (root == null) return emptyList()
        val result = mutableListOf<List<Int>>()
        val queue = ArrayDeque<TreeNode>()
        queue.add(root)
        var leftToRight = true
        while (queue.isNotEmpty()) {
            val level = mutableListOf<Int>()
            repeat(queue.size) {
                val node = queue.removeFirst()
                level.add(node.`val`)
                node.left?.let { queue.add(it) }
                node.right?.let { queue.add(it) }
            }
            if (!leftToRight) level.reverse()
            result.add(level)
            leftToRight = !leftToRight
        }
        return result
    }
}
