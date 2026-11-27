// LeetCode 2327. Number of People Aware of a Secret — Medium
// https://leetcode.com/problems/number-of-people-aware-of-a-secret/
// Submission 2204700439 — Accepted, TypeScript
//
// My thinking: same idea as the Python version — dp[i] counts who first
// learns the secret on day i, a prefix sum makes each day's window sum
// O(1), and the answer is everyone who learned it within the last
// `forget` days.
function peopleAwareOfSecret(n: number, delay: number, forget: number): number {
    const MOD = 1000000007;
    const dp: number[] = new Array(n + 1).fill(0);
    dp[1] = 1;
    const pref: number[] = new Array(n + 1).fill(0);
    pref[1] = 1;
    for (let i = 2; i <= n; i++) {
        const lo = Math.max(1, i - forget + 1);
        const hi = i - delay;
        if (hi >= lo) {
            dp[i] = (pref[hi] - pref[lo - 1] + MOD) % MOD;
        }
        pref[i] = (pref[i - 1] + dp[i]) % MOD;
    }
    return (pref[n] - pref[Math.max(0, n - forget)] + MOD) % MOD;
};
