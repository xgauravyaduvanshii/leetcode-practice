// LeetCode 116. Populating Next Right Pointers in Each Node — Medium
// https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
// Submission 2204009219 — Accepted, Java

// My thinking: the tree is perfect, so every node has two children and
// every level is full. I walk level by level using the next pointers I
// have already set, which costs no extra space. I start each level at
// its leftmost node and move right along the next pointers. For every
// node I meet, I link its left child to its right child, and its right
// child to the left child of the next node on the same level (or to
// nothing if there is no next node). Once a level is fully linked I
// drop down to its leftmost child and do the next level the same way.
// An empty tree needs no links at all.
class Solution {
    public Node connect(Node root) {
        if (root == null) {
            return root;
        }
        Node leftmost = root;
        while (leftmost.left != null) {
            Node node = leftmost;
            while (node != null) {
                node.left.next = node.right;
                if (node.next != null) {
                    node.right.next = node.next.left;
                }
                node = node.next;
            }
            leftmost = leftmost.left;
        }
        return root;
    }
}
