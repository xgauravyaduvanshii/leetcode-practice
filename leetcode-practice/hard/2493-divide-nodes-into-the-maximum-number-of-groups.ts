// LeetCode 2493. Divide Nodes Into the Maximum Number of Groups — Hard
// https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/
// Submission 2201779372 — Accepted, TypeScript
//
// My thinking: neighbours must sit in
// groups exactly one apart, so each
// connected piece has to be bipartite —
// an odd cycle makes the whole thing
// impossible — and the most groups a piece
// can take is its longest shortest path
// plus one, which I find by walking out
// from every node in the piece.

function magnificentSets(n: number, edges: number[][]): number {
  const adj: number[][] = Array.from({ length: n }, () => []);
  for (const [a, b] of edges) {
    adj[a - 1].push(b - 1);
    adj[b - 1].push(a - 1);
  }

  function bfs(start: number): Map<number, number> {
    const dist = new Map<number, number>([[start, 0]]);
    const q: number[] = [start];
    while (q.length > 0) {
      const u = q.shift()!;
      for (const w of adj[u]) {
        if (!dist.has(w)) {
          dist.set(w, dist.get(u)! + 1);
          q.push(w);
        }
      }
    }
    return dist;
  }

  const seen = new Array<boolean>(n).fill(false);
  let total = 0;
  for (let s = 0; s < n; s++) {
    if (seen[s]) continue;
    const comp = bfs(s);
    for (const v of comp.keys()) seen[v] = true;
    for (const v of comp.keys()) {
      for (const w of adj[v]) {
        if (comp.get(v)! % 2 === comp.get(w)! % 2) return -1;
      }
    }
    let best = 0;
    for (const v of comp.keys()) {
      const d = bfs(v);
      for (const x of d.values()) best = Math.max(best, x);
    }
    total += best + 1;
  }
  return total;
}
