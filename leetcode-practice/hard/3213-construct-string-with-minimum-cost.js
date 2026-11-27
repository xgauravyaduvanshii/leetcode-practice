// LeetCode 3213. Construct String with Minimum Cost — Hard
// https://leetcode.com/problems/construct-string-with-minimum-cost/
// Submission 2202097608 — Accepted, JavaScript
//
// My thinking: I dedupe the words, keeping
// the cheapest cost per word, then run a
// DP over the target: dp[i] is the cheapest
// cost to build the first i characters.
// Matching words at each position is a
// trie walk, except when words are very
// long — then I precompute every
// occurrence with string search instead.
// The hybrid keeps both the long-word and
// the many-occurrence cases inside the
// limits.

/**
 * @param {string} target
 * @param {string[]} words
 * @param {number[]} costs
 * @return {number}
 */
var minimumCost = function(target, words, costs) {
    const best = new Map();
    for (let i = 0; i < words.length; i++) {
        if (!best.has(words[i]) || costs[i] < best.get(words[i])) best.set(words[i], costs[i]);
    }
    const n = target.length;
    const INF = 1e18;
    const dp = new Array(n + 1).fill(INF);
    dp[0] = 0;
    let maxLen = 0;
    for (const w of best.keys()) maxLen = Math.max(maxLen, w.length);
    let useFind = false;
    if (maxLen > 300) {
        let total = 0;
        for (const w of best.keys()) {
            total += n - w.length + 1;
            if (total > 1500000) break;
        }
        if (total <= 1500000) useFind = true;
    }
    if (useFind) {
        const trans = Array.from({length: n}, () => []);
        for (const [w, c] of best) {
            const L = w.length;
            if (L > n) continue;
            let start = 0;
            while (true) {
                const idx = target.indexOf(w, start);
                if (idx < 0) break;
                trans[idx].push([idx + L, c]);
                start = idx + 1;
            }
        }
        for (let i = 0; i < n; i++) {
            if (dp[i] === INF) continue;
            for (const [j, c] of trans[i]) {
                const nd = dp[i] + c;
                if (nd < dp[j]) dp[j] = nd;
            }
        }
        return dp[n] === INF ? -1 : dp[n];
    }
    const children = [{}];
    const end = [-1];
    for (const [w, c] of best) {
        let node = 0;
        for (const ch of w) {
            let nxt = children[node][ch];
            if (nxt === undefined) {
                nxt = children.length;
                children[node][ch] = nxt;
                children.push({});
                end.push(-1);
            }
            node = nxt;
        }
        if (end[node] === -1 || c < end[node]) end[node] = c;
    }
    for (let i = 0; i < n; i++) {
        if (dp[i] === INF) continue;
        let node = 0;
        const upper = Math.min(n, i + maxLen);
        for (let j = i; j < upper; j++) {
            const nxt = children[node][target[j]];
            if (nxt === undefined) break;
            node = nxt;
            const c = end[node];
            if (c !== -1) {
                const nd = dp[i] + c;
                if (nd < dp[j + 1]) dp[j + 1] = nd;
            }
        }
    }
    return dp[n] === INF ? -1 : dp[n];
};
