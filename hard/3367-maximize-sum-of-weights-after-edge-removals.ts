// LeetCode 3367. Maximize Sum of Weights after Edge Removals — Hard
// https://leetcode.com/problems/maximize-sum-of-weights-after-edge-removals/
// Submission 2202428266 -- Accepted, TypeScript
function maximizeSumOfWeights(edges: number[][], k: number): number {
    // My thinking: root the tree at 0. For each node I decide which child
    // edges to keep: keeping edge (u,v) gains w + dp1(v) - dp0(v) over
    // dropping it, where dp0/dp1 are the best sums in v's subtree with v's
    // parent edge dropped/taken. A node keeps at most k child edges (k-1 if
    // its own parent edge is kept), so I take the largest positive gains up
    // to that limit. I process nodes bottom-up with an explicit order to
    // avoid recursion limits.
    const n = edges.length + 1;
    const adj: [number, number][][] = Array.from({length: n}, () => []);
    for (const [u, v, w] of edges) {
        adj[u].push([v, w]);
        adj[v].push([u, w]);
    }
    const parent = new Array(n).fill(-1);
    parent[0] = -2;
    const order: number[] = [0];
    for (const u of order) {
        for (const [v, w] of adj[u]) {
            if (parent[v] === -1) {
                parent[v] = u;
                order.push(v);
            }
        }
    }
    const dp0 = new Array(n).fill(0);
    const dp1 = new Array(n).fill(0);
    for (let idx = order.length - 1; idx >= 0; idx--) {
        const u = order[idx];
        const gains: number[] = [];
        let base = 0;
        for (const [v, w] of adj[u]) {
            if (parent[v] === u) {
                base += dp0[v];
                gains.push(w + dp1[v] - dp0[v]);
            }
        }
        gains.sort((a, b) => b - a);
        let s0 = base, take = 0;
        for (const g of gains) {
            if (take >= k || g <= 0) break;
            s0 += g;
            take++;
        }
        dp0[u] = s0;
        let s1 = base;
        take = 0;
        for (const g of gains) {
            if (take >= k - 1 || g <= 0) break;
            s1 += g;
            take++;
        }
        dp1[u] = s1;
    }
    return dp0[0];
}
