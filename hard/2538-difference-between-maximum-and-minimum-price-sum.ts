// LeetCode 2538. Difference Between Maximum and Minimum Price Sum — Hard
// https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/
// Submission 2201804759 — Accepted, TypeScript
//
// My thinking: from any root the
// cheapest path is the root alone, so
// the cost is just the dearest path
// starting there minus the root's own
// price — I learn the best downward
// walk from every node and the best walk
// coming in from above, then take the
// widest gap.

function maxOutput(n: number, edges: number[][], price: number[]): number {
  const adj: number[][] = Array.from({ length: n }, () => []);
  for (const [a, b] of edges) {
    adj[a].push(b);
    adj[b].push(a);
  }
  const down: number[] = new Array(n).fill(0);
  const up: number[] = new Array(n).fill(0);
  const parent: number[] = new Array(n).fill(-1);
  const order: number[] = [0];
  parent[0] = -2;
  for (const u of order) {
    for (const w of adj[u]) {
      if (parent[w] === -1) {
        parent[w] = u;
        order.push(w);
      }
    }
  }
  for (let i = order.length - 1; i >= 0; i--) {
    const u = order[i];
    let best = 0;
    for (const w of adj[u]) {
      if (parent[w] === u) best = Math.max(best, down[w]);
    }
    down[u] = price[u] + best;
  }
  for (const u of order) {
    let top1 = 0;
    let top2 = 0;
    for (const w of adj[u]) {
      if (parent[w] === u) {
        if (down[w] > top1) {
          top2 = top1;
          top1 = down[w];
        } else if (down[w] > top2) {
          top2 = down[w];
        }
      }
    }
    for (const w of adj[u]) {
      if (parent[w] === u) {
        const use = down[w] !== top1 ? top1 : top2;
        up[w] = price[w] + Math.max(up[u], price[u] + use);
      }
    }
  }
  let ans = 0;
  for (let u = 0; u < n; u++) {
    ans = Math.max(ans, Math.max(down[u], up[u]) - price[u]);
  }
  return ans;
}
