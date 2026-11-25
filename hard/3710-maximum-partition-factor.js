// LeetCode 3710. Maximum Partition Factor — Hard
// https://leetcode.com/problems/maximum-partition-factor/
// Submission 2203058386 — Accepted, JavaScript
/**
 * @param {number[][]} points
 * @return {number}
 */
var maximumPartitionFactor = function(points) {
    // My thinking: binary-search-free. A split has factor at
    // least D exactly when every pair closer than D lands in
    // different groups, i.e. when the graph joining pairs
    // with distance < D is bipartite. As D grows, edges join
    // in order of distance, so the best D is the distance of
    // the first edge that closes an odd cycle. I add the
    // edges shortest first with a parity union-find (each
    // component remembers which side each point is on); the
    // first edge whose ends are already forced onto the same
    // side is the answer. With two points the factor is 0
    // by definition.
    const n = points.length;
    if (n === 2) return 0;
    const edges = [];
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            const d = Math.abs(points[i][0] - points[j][0])
                + Math.abs(points[i][1] - points[j][1]);
            edges.push([d, i, j]);
        }
    }
    edges.sort((a, b) => a[0] - b[0]);
    const parent = Array.from({ length: n }, (_, i) => i);
    const parity = new Array(n).fill(0);

    const find = (x) => {
        if (parent[x] !== x) {
            const [root, p] = find(parent[x]);
            parity[x] ^= p;
            parent[x] = root;
        }
        return [parent[x], parity[x]];
    };

    for (const [d, u, v] of edges) {
        const [ru, pu] = find(u);
        const [rv, pv] = find(v);
        if (ru === rv) {
            if (pu === pv) return d;
        } else {
            // Join the components so that u and v end up on
            // opposite sides: parity(ru -> rv) = pu ^ pv ^ 1.
            parent[ru] = rv;
            parity[ru] = pu ^ pv ^ 1;
        }
    }
    return edges[edges.length - 1][0];
};
