// LeetCode 1857. Largest Color Value in a Directed Graph — Hard
// https://leetcode.com/problems/largest-color-value-in-a-directed-graph/
// Submission 2201205064 — Accepted, JavaScript
//
// My thinking: I walk the graph in topological
// order, carrying for every node the best count
// of each colour on any path reaching it — if
// some node is never reached the graph has a
// cycle and the answer is minus one.

function largestPathValue(colors, edges) {
    const n = colors.length;
    const graph = Array.from({ length: n }, () => []);
    const indeg = new Array(n).fill(0);
    for (const [u, v] of edges) {
        graph[u].push(v);
        indeg[v]++;
    }
    const dp = Array.from({ length: n }, () => new Array(26).fill(0));
    const q = [];
    for (let i = 0; i < n; i++) if (indeg[i] === 0) q.push(i);
    let seen = 0;
    let ans = 0;
    while (q.length > 0) {
        const u = q.shift();
        seen++;
        dp[u][colors.charCodeAt(u) - 97]++;
        ans = Math.max(ans, Math.max(...dp[u]));
        for (const v of graph[u]) {
            for (let c = 0; c < 26; c++) {
                if (dp[u][c] > dp[v][c]) dp[v][c] = dp[u][c];
            }
            indeg[v]--;
            if (indeg[v] === 0) q.push(v);
        }
    }
    return seen < n ? -1 : ans;
}
