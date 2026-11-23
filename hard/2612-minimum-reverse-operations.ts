// LeetCode 2612. Minimum Reverse Operations — Hard
// https://leetcode.com/problems/minimum-reverse-operations/
// Submission 2201851366 — Accepted, TypeScript
//
// My thinking: reversing a window of
// length k throws the single 1 to a
// mirror spot, and every mirror spot in
// reach shares one parity — so I keep
// the untouched spots of each parity in
// a chain that always points at the next
// one, and sweep them up the moment a
// window can reach them.

function minReverseOperations(n: number, p: number, banned: number[], k: number): number[] {
  const ans: number[] = new Array(n).fill(-1);
  ans[p] = 0;
  const bannedSet = new Set(banned);
  // DSU "next unvisited" chains, one per parity, over the index y // 2.
  const size = Math.floor((n + 1) / 2) + 1;
  const parent: number[][] = [Array.from({ length: size }, (_, i) => i), Array.from({ length: size }, (_, i) => i)];
  const find = (par: number[], x: number): number => {
    while (par[x] !== x) {
      par[x] = par[par[x]];
      x = par[x];
    }
    return x;
  };
  const remove = (par: number[], y: number): void => {
    const i = Math.floor(y / 2);
    par[i] = find(par, i + 1);
  };
  for (const b of bannedSet) remove(parent[b & 1], b);
  remove(parent[p & 1], p);
  const q: number[] = [p];
  let head = 0;
  while (head < q.length) {
    const x = q[head++];
    const lMin = Math.max(0, x - k + 1);
    const lMax = Math.min(x, n - k);
    const yMin = 2 * lMin + k - 1 - x;
    const yMax = 2 * lMax + k - 1 - x;
    const parity = (k - 1 - x) & 1;
    const par = parent[parity];
    const start = (yMin & 1) === parity ? yMin : yMin + 1;
    let i = find(par, Math.floor(start / 2));
    while (true) {
      const y = 2 * i + parity;
      if (y > yMax || i >= size - 1) break;
      ans[y] = ans[x] + 1;
      q.push(y);
      remove(par, y);
      i = find(par, i);
    }
  }
  return ans;
}
