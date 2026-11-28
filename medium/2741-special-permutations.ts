// LeetCode 2741. Special Permutations — Medium
// https://leetcode.com/problems/special-permutations/
// Submission 2205228653 — Accepted, TypeScript
//
// My thinking: same idea as the Python version — DP over
// subsets, extending each partial permutation only with an
// unused element that divides or is divisible by the last one.
function specialPerm(nums: number[]): number {
    const MOD = 1e9 + 7;
    const n = nums.length;
    const dp: number[][] = Array.from({ length: 1 << n }, () => new Array(n).fill(0));
    for (let i = 0; i < n; i++) dp[1 << i][i] = 1;
    for (let mask = 0; mask < (1 << n); mask++) {
        for (let last = 0; last < n; last++) {
            if (dp[mask][last] === 0) continue;
            for (let nxt = 0; nxt < n; nxt++) {
                if ((mask >> nxt) & 1) continue;
                if (nums[last] % nums[nxt] === 0 || nums[nxt] % nums[last] === 0) {
                    dp[mask | (1 << nxt)][nxt] = (dp[mask | (1 << nxt)][nxt] + dp[mask][last]) % MOD;
                }
            }
        }
    }
    return dp[(1 << n) - 1].reduce((a, b) => (a + b) % MOD, 0);
}
