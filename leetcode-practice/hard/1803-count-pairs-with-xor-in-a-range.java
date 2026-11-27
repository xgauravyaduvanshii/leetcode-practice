// LeetCode 1803. Count Pairs With XOR in a Range — Hard
// https://leetcode.com/problems/count-pairs-with-xor-in-a-range/
// Submission 2201175051 — Accepted, Java
//
// My thinking: pairs with xor below a limit are
// counted by walking a binary trie bit by bit —
// whenever the limit has a 1, the whole branch
// that keeps the xor's bit 0 counts at once. I
// take the count below high + 1 minus the count
// below low.

class Solution {
    private static class Node {
        Node[] child = new Node[2];
        int count = 0;
    }

    public int countPairs(int[] nums, int low, int high) {
        return countLess(nums, high + 1) - countLess(nums, low);
    }

    private int countLess(int[] nums, int limit) {
        Node root = new Node();
        int total = 0;
        for (int x : nums) {
            total += query(root, x, limit);
            insert(root, x);
        }
        return total;
    }

    private void insert(Node root, int x) {
        Node node = root;
        node.count++;
        for (int b = 15; b >= 0; b--) {
            int bit = (x >> b) & 1;
            if (node.child[bit] == null) node.child[bit] = new Node();
            node = node.child[bit];
            node.count++;
        }
    }

    private int query(Node root, int x, int limit) {
        Node node = root;
        int total = 0;
        for (int b = 15; b >= 0; b--) {
            if (node == null) break;
            int bitX = (x >> b) & 1;
            int bitL = (limit >> b) & 1;
            if (bitL == 1) {
                if (node.child[bitX] != null) total += node.child[bitX].count;
                node = node.child[1 - bitX];
            } else {
                node = node.child[bitX];
            }
        }
        return total;
    }
}
