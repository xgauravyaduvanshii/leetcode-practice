// LeetCode 3615. Longest Palindromic Path in Graph — Hard
// https://leetcode.com/problems/longest-palindromic-path-in-graph/
// Submission 2202875332 — Accepted, JavaScript
var maxLen = function(n, edges, label) {
    // My thinking: with at most 14 nodes I keep, for every set
    // of visited nodes, the pairs of endpoints of palindromic
    // paths using exactly that set. A single node is a
    // palindrome of length 1, and an edge whose ends share a
    // label is one of length 2. From any such path I grow it by
    // one node at each end, but only when the two new labels
    // match. I process the sets in increasing size so every
    // extension is itself extended later; the answer is the
    // largest set that holds a palindrome.
    const adj = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }
    const dp = new Map();
    function add(mask, pair) {
        if (!dp.has(mask)) dp.set(mask, new Set());
        dp.get(mask).add(pair[0] * n + pair[1]);
    }
    for (let u = 0; u < n; u++) add(1 << u, [u, u]);
    for (const [u, v] of edges) {
        if (label[u] === label[v]) {
            add((1 << u) | (1 << v), [u, v]);
            add((1 << u) | (1 << v), [v, u]);
        }
    }
    const popcount = (m) => {
        let c = 0;
        while (m) { c += m & 1; m >>= 1; }
        return c;
    };
    let best = n >= 1 ? 1 : 0;
    for (let pc = 1; pc <= n; pc++) {
        for (let mask = 0; mask < (1 << n); mask++) {
            if (popcount(mask) !== pc) continue;
            const pairs = dp.get(mask);
            if (!pairs) continue;
            if (pc > best) best = pc;
            for (const code of [...pairs]) {
                const u = Math.floor(code / n), v = code % n;
                for (const a of adj[u]) {
                    if (mask & (1 << a)) continue;
                    for (const b of adj[v]) {
                        if ((mask & (1 << b)) || a === b) continue;
                        if (label[a] === label[b]) add(mask | (1 << a) | (1 << b), [a, b]);
                    }
                }
            }
        }
    }
    for (const mask of dp.keys()) best = Math.max(best, popcount(mask));
    return best;
};
