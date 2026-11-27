// LeetCode 3108. Minimum Cost Walk in Weighted Graph — Hard
// https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/
// Submission 2201997669 — Accepted, TypeScript
//
// My thinking: I union the edges with a
// disjoint set, keeping the bitwise AND
// of all edge weights in each component.
// Two vertices can walk together exactly
// when they share a component, and then
// the cheapest walk costs the
// component's AND; otherwise the answer
// is -1.

function minimumCost(n: number, edges: number[][], query: number[][]): number[] {
    const parent: number[] = Array.from({ length: n }, (_, i) => i);
    const compAnd: number[] = new Array(n).fill(-1);
    function find(x: number): number {
        while (parent[x] !== x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }
    for (const [u, v, w] of edges) {
        const ru = find(u), rv = find(v);
        if (ru === rv) {
            compAnd[ru] &= w;
        } else {
            parent[rv] = ru;
            compAnd[ru] = compAnd[ru] & compAnd[rv] & w;
        }
    }
    const ans: number[] = [];
    for (const [s, t] of query) {
        const rs = find(s), rt = find(t);
        ans.push(rs !== rt ? -1 : compAnd[rs]);
    }
    return ans;
};
