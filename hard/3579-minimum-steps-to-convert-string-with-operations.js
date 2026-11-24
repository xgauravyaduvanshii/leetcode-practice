// LeetCode 3579. Minimum Steps to Convert String with Operations — Hard
// https://leetcode.com/problems/minimum-steps-to-convert-string-with-operations/
// Submission 2202861513 — Accepted, JavaScript
var minOperations = function(word1, word2) {
    // My thinking: I split the strings into blocks and price
    // each block on its own. Inside a block, a swap only helps
    // when it fixes both ends (a and b sitting in each other's
    // places), so the best I can do is pair up as many of those
    // as possible and replace the rest; a single reverse costs
    // one extra operation and is worth it only when the reversed
    // block is cheaper to finish. A DP over the split points
    // picks the cheapest blocks.
    const n = word1.length;
    function costNoRev(S, T) {
        let m = 0;
        const cnt = Array.from({ length: 26 }, () => new Array(26).fill(0));
        for (let i = 0; i < S.length; i++) {
            if (S[i] !== T[i]) {
                m++;
                cnt[S.charCodeAt(i) - 97][T.charCodeAt(i) - 97]++;
            }
        }
        let swaps = 0;
        for (let a = 0; a < 26; a++) {
            for (let b = a + 1; b < 26; b++) swaps += Math.min(cnt[a][b], cnt[b][a]);
        }
        return m - swaps;
    }
    function cost(l, r) {
        const S = word1.slice(l, r + 1);
        const T = word2.slice(l, r + 1);
        const rev = S.split('').reverse().join('');
        return Math.min(costNoRev(S, T), 1 + costNoRev(rev, T));
    }
    const dp = new Array(n + 1).fill(1e9);
    dp[0] = 0;
    for (let i = 1; i <= n; i++) {
        for (let j = 0; j < i; j++) dp[i] = Math.min(dp[i], dp[j] + cost(j, i - 1));
    }
    return dp[n];
};
