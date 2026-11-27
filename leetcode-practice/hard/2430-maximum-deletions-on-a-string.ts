// LeetCode 2430. Maximum Deletions on a String — Hard
// https://leetcode.com/problems/maximum-deletions-on-a-string/
// Submission 2201738439 — Accepted, TypeScript
//
// My thinking: deleting more means cutting
// smaller matching pieces — I first learn
// how long any two suffixes agree, then
// from each position I take the best cut
// whose two halves match, or just sweep
// the rest away in one go.

function deleteString(s: string): number {
    const n = s.length;
    const lcp: number[][] = Array.from({ length: n + 1 }, () => new Array(n + 1).fill(0));
    for (let i = n - 1; i >= 0; i--) {
        for (let j = n - 1; j >= 0; j--) {
            if (s[i] === s[j]) lcp[i][j] = lcp[i + 1][j + 1] + 1;
        }
    }
    const dp = new Array(n + 1).fill(0);
    for (let i = n - 1; i >= 0; i--) {
        let best = 0;
        const maxJ = Math.floor((n - i) / 2);
        for (let j = 1; j <= maxJ; j++) {
            if (lcp[i][i + j] >= j) best = Math.max(best, dp[i + j]);
        }
        dp[i] = best + 1;
    }
    return dp[0];
}
