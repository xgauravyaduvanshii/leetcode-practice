// LeetCode 2699. Modify Graph Edge Weights — Hard
// https://leetcode.com/problems/modify-graph-edge-weights/
// Submission 2201871679 — Accepted, TypeScript
//
// My thinking: if the fixed roads
// alone already beat the target there
// is nothing to do, and if the cheapest
// road with every -1 set to 1 already
// overshoots, it can never be done — so
// I take the cheapest road, stretch one
// of its -1 edges until that road is
// exactly the target, price every -1
// that is not on that road out of the
// way, and check the road really
// measures the target.

function modifiedGraphEdges(n: number, edges: number[][], source: number, destination: number, target: number): number[][] {
  const INF = Infinity;
  function dijkstra(adj: [number, number, number][][], src: number): { dist: number[]; prev: ([number, number] | -1)[] } {
    const dist: number[] = new Array(n).fill(INF);
    const prev: ([number, number] | -1)[] = new Array(n).fill(-1);
    dist[src] = 0;
    const pq: [number, number][] = [[0, src]];
    const push = (d: number, u: number) => {
      pq.push([d, u]);
      let i = pq.length - 1;
      while (i > 0) {
        const p = Math.floor((i - 1) / 2);
        if (pq[p][0] <= pq[i][0]) break;
        [pq[p], pq[i]] = [pq[i], pq[p]];
        i = p;
      }
    };
    const pop = (): [number, number] => {
      const top = pq[0];
      const last = pq.pop()!;
      if (pq.length > 0) {
        pq[0] = last;
        let i = 0;
        for (;;) {
          const l = 2 * i + 1, r = 2 * i + 2;
          let s = i;
          if (l < pq.length && pq[l][0] < pq[s][0]) s = l;
          if (r < pq.length && pq[r][0] < pq[s][0]) s = r;
          if (s === i) break;
          [pq[s], pq[i]] = [pq[i], pq[s]];
          i = s;
        }
      }
      return top;
    };
    while (pq.length > 0) {
      const [d, u] = pop();
      if (d !== dist[u]) continue;
      for (const [v, w, ei] of adj[u]) {
        const nd = d + w;
        if (nd < dist[v]) {
          dist[v] = nd;
          prev[v] = [u, ei];
          push(nd, v);
        }
      }
    }
    return { dist, prev };
  }
  function build(weights: number[]): [number, number, number][][] {
    const adj: [number, number, number][][] = Array.from({ length: n }, () => []);
    edges.forEach(([a, b], ei) => {
      const wt = weights[ei];
      adj[a].push([b, wt, ei]);
      adj[b].push([a, wt, ei]);
    });
    return adj;
  }
  const w1 = edges.map(([, , w]) => (w > 0 ? w : 1));
  const { dist: d1, prev } = dijkstra(build(w1), source);
  if (d1[destination] > target) return [];
  if (d1[destination] === target) return edges.map(([a, b, w]) => [a, b, w > 0 ? w : 1]);
  const pathEdges: number[] = [];
  let cur = destination;
  while (cur !== source && prev[cur] !== -1) {
    const [u, ei] = prev[cur] as [number, number];
    pathEdges.push(ei);
    cur = u;
  }
  if (cur !== source) return [];
  const pathNeg = pathEdges.filter((ei) => edges[ei][2] === -1);
  if (pathNeg.length === 0) return [];
  const fixedAdj: [number, number, number][][] = Array.from({ length: n }, () => []);
  edges.forEach(([a, b, w], ei) => {
    if (w > 0) {
      fixedAdj[a].push([b, w, ei]);
      fixedAdj[b].push([a, w, ei]);
    }
  });
  const { dist: dFixed } = dijkstra(fixedAdj, source);
  if (dFixed[destination] < target) return [];
  const onPath = new Set(pathEdges);
  for (const adjust of pathNeg) {
    const extra = target - d1[destination];
    const weights = edges.map(([a, b, w], ei) => {
      if (w > 0) return w;
      if (ei === adjust) return 1 + extra;
      if (onPath.has(ei)) return 1;
      return 2000000000;
    });
    const adj = build(weights);
    if (dijkstra(adj, source).dist[destination] === target) {
      return edges.map(([a, b], ei) => [a, b, weights[ei]]);
    }
  }
  return [];
}
