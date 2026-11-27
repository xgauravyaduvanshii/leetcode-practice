// LeetCode 3327. Check if DFS Strings Are Palindromes — Hard
// https://leetcode.com/problems/check-if-dfs-strings-are-palindromes/
// Submission 2202377196 — Accepted, JavaScript
//
// My thinking: the DFS string of a node is the concatenation of its
// children's DFS strings (children in increasing order) followed by its own
// character, so in one post-order walk of the whole tree each subtree
// occupies one contiguous interval, ending at the node's own position. I
// record that interval per node, then answer every palindrome query in O(1)
// with a double rolling hash (BigInt, so the modular multiplications stay
// exact): a substring is a palindrome exactly when its forward hash equals
// the hash of the same interval read on the reversed string.

/**
 * @param {number[]} parent
 * @param {string} s
 * @return {boolean[]}
 */
var findAnswer = function(parent, s) {
    const MOD1 = 1000000007n, MOD2 = 1000000009n, BASE = 9113823n;
    const n = parent.length;
    const children = Array.from({length: n}, () => []);
    for (let i = 1; i < n; i++) children[parent[i]].push(i);

    const order = [];
    const pos = new Array(n), size = new Array(n);
    const stack = [[0, false]];
    while (stack.length) {
        const [u, done] = stack.pop();
        if (done) {
            pos[u] = order.length;
            order.push(s[u]);
            let sz = 1;
            for (const c of children[u]) sz += size[c];
            size[u] = sz;
        } else {
            stack.push([u, true]);
            for (let i = children[u].length - 1; i >= 0; i--) {
                stack.push([children[u][i], false]);
            }
        }
    }

    const t = order.join('');
    const rev = t.split('').reverse().join('');

    function build(text) {
        const h1 = new Array(n + 1).fill(0n), h2 = new Array(n + 1).fill(0n);
        for (let i = 0; i < n; i++) {
            const v = BigInt(text.charCodeAt(i));
            h1[i + 1] = (h1[i] * BASE + v) % MOD1;
            h2[i + 1] = (h2[i] * BASE + v) % MOD2;
        }
        return [h1, h2];
    }
    const [h1, h2] = build(t);
    const [r1, r2] = build(rev);
    const pow1 = new Array(n + 1).fill(1n), pow2 = new Array(n + 1).fill(1n);
    for (let i = 1; i <= n; i++) {
        pow1[i] = pow1[i - 1] * BASE % MOD1;
        pow2[i] = pow2[i - 1] * BASE % MOD2;
    }
    const get = (h, p, mod, l, r) => (h[r + 1] - h[l] * p[r - l + 1] % mod + mod) % mod;

    const ans = [];
    for (let u = 0; u < n; u++) {
        const l = pos[u] - size[u] + 1, r = pos[u];
        const rl = n - 1 - r, rr = n - 1 - l;
        ans.push(get(h1, pow1, MOD1, l, r) === get(r1, pow1, MOD1, rl, rr) &&
                 get(h2, pow2, MOD2, l, r) === get(r2, pow2, MOD2, rl, rr));
    }
    return ans;
};
