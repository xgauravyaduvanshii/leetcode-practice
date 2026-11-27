// LeetCode 2097. Valid Arrangement of Pairs — Hard
// https://leetcode.com/problems/valid-arrangement-of-pairs/
// Submission 2201571513 — Accepted, TypeScript
//
// My thinking: the pairs are the edges of a
// directed graph and the arrangement is a walk
// that uses every edge once, so I follow
// Hierholzer — always take an unused edge
// forward, and backtrack into the answer when
// a stop runs out of edges.

function validArrangement(pairs: number[][]): number[][] {
    const graph = new Map<number, number[]>();
    const indeg = new Map<number, number>();
    const outdeg = new Map<number, number>();
    for (const [u, v] of pairs) {
        if (!graph.has(u)) graph.set(u, []);
        graph.get(u)!.push(v);
        outdeg.set(u, (outdeg.get(u) ?? 0) + 1);
        indeg.set(v, (indeg.get(v) ?? 0) + 1);
    }
    let start = pairs[0][0];
    for (const u of graph.keys()) {
        if ((outdeg.get(u) ?? 0) - (indeg.get(u) ?? 0) === 1) {
            start = u;
            break;
        }
    }
    const stack: number[] = [start];
    const path: number[] = [];
    while (stack.length > 0) {
        const u = stack[stack.length - 1];
        const edges = graph.get(u) ?? [];
        if (edges.length > 0) {
            stack.push(edges.pop()!);
        } else {
            path.push(stack.pop()!);
        }
    }
    path.reverse();
    const ans: number[][] = [];
    for (let i = 0; i + 1 < path.length; i++) ans.push([path[i], path[i + 1]]);
    return ans;
}
