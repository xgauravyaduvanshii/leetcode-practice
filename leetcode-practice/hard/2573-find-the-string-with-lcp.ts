// LeetCode 2573. Find the String with LCP — Hard
// https://leetcode.com/problems/find-the-string-with-lcp/
// Submission 2201828089 — Accepted, TypeScript
//
// My thinking: equal prefixes mean
// equal letters, so I tie together every
// pair the matrix says must match, check
// the matrix agrees with itself going
// down the diagonal, and then hand out
// the smallest letters that keep the
// zero entries apart.

function findTheString(lcp: number[][]): string {
  const n = lcp.length;
  const parent = Array.from({ length: n }, (_, i) => i);
  const find = (x: number): number => {
    while (parent[x] !== x) {
      parent[x] = parent[parent[x]];
      x = parent[x];
    }
    return x;
  };
  const union = (a: number, b: number): void => {
    const ra = find(a);
    const rb = find(b);
    if (ra !== rb) parent[ra] = rb;
  };
  for (let i = 0; i < n; i++) {
    if (lcp[i][i] !== n - i) return "";
    for (let j = 0; j < n; j++) {
      if (lcp[i][j] !== lcp[j][i]) return "";
      if (lcp[i][j] > Math.min(n - i, n - j)) return "";
      if (lcp[i][j] > 0) {
        union(i, j);
        if (i + 1 < n && j + 1 < n) {
          if (lcp[i + 1][j + 1] !== lcp[i][j] - 1) return "";
        } else if (lcp[i][j] !== 1) {
          return "";
        }
      }
    }
  }
  const word: string[] = new Array(n).fill("");
  for (let i = 0; i < n; i++) {
    if (word[i]) continue;
    const used = new Set<string>();
    for (let j = 0; j < i; j++) {
      if (word[j] && find(j) !== find(i) && lcp[i][j] === 0) used.add(word[j]);
    }
    for (let j = 0; j < n; j++) {
      if (find(j) === find(i) && word[j] && used.has(word[j])) return "";
    }
    let code = 97;
    while (used.has(String.fromCharCode(code))) code++;
    if (code > 122) return "";
    const c = String.fromCharCode(code);
    for (let j = 0; j < n; j++) {
      if (find(j) === find(i)) word[j] = c;
    }
  }
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (lcp[i][j] === 0 && word[i] === word[j]) return "";
    }
  }
  return word.join("");
}
