// LeetCode 3553. Minimum Weighted Subgraph With the Required Paths II — Hard
// https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths-ii/
// Submission 2202840193 — Accepted, JavaScript
var minimumWeight = function(edges, queries) {
    // My thinking: the cheapest subtree that reaches dest from
    // both sources is the union of the two paths to dest, which
    // is the smallest subtree spanning all three nodes. Its
    // weight is half the sum of the three pairwise distances —
    // each edge of that subtree is counted in exactly two of
    // them. Distances come from root distances and binary-lifted
    // lowest common ancestors.
    let n = 0;
    for (const [u, v] of edges) n = Math.max(n, u, v);
    n += 1;
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v, w] of edges) {
        adj[u].push([v, w]);
        adj[v].push([u, w]);
    }
    const LOG = 18;
    const up = Array.from({ length: LOG }, () => new Array(n).fill(0));
    const depth = new Array(n).fill(0);
    const dist = new Array(n).fill(0);
    const parent = new Array(n).fill(-1);
    const order = [0];
    parent[0] = -2;
    for (let i = 0; i < order.length; i++) {
        const u = order[i];
        for (const [v, w] of adj[u]) {
            if (parent[v] === -1) {
                parent[v] = u;
                depth[v] = depth[u] + 1;
                dist[v] = dist[u] + w;
                up[0][v] = u;
                order.push(v);
            }
        }
    }
    for (let k = 1; k < LOG; k++) {
        for (let i = 0; i < n; i++) up[k][i] = up[k - 1][up[k - 1][i]];
    }
    function lca(u, v) {
        if (depth[u] < depth[v]) [u, v] = [v, u];
        let diff = depth[u] - depth[v];
        let bit = 0;
        while (diff) {
            if (diff & 1) u = up[bit][u];
            diff >>= 1;
            bit++;
        }
        if (u === v) return u;
        for (let k = LOG - 1; k >= 0; k--) {
            if (up[k][u] !== up[k][v]) { u = up[k][u]; v = up[k][v]; }
        }
        return up[0][u];
    }
    function d(u, v) {
        const w = lca(u, v);
        return dist[u] + dist[v] - 2 * dist[w];
    }
    return queries.map(([s1, s2, dest]) => Math.floor((d(s1, s2) + d(s2, dest) + d(s1, dest)) / 2));
};
