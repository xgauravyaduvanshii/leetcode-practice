// LeetCode 133. Clone Graph — Medium
// https://leetcode.com/problems/clone-graph/
// Submission 2204035348 — Accepted, Java

// My thinking: I walk the graph once with a depth-first search,
// remembering each original node and its clone in a map. When I
// first meet a node I make its clone, then I clone each neighbour
// the same way and link the clones together. The map stops me
// from cloning the same node twice, which is what breaks the
// cycles — a node I have already seen just returns its clone.
import java.util.*;

class Solution {
    private Map<Node, Node> oldToNew = new HashMap<>();

    public Node cloneGraph(Node node) {
        if (node == null) {
            return null;
        }
        if (oldToNew.containsKey(node)) {
            return oldToNew.get(node);
        }
        Node copy = new Node(node.val);
        oldToNew.put(node, copy);
        for (Node neighbour : node.neighbors) {
            copy.neighbors.add(cloneGraph(neighbour));
        }
        return copy;
    }
}
