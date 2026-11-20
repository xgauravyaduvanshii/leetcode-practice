function minInsertions(s: string): number {
    // My thinking: the insertions needed are whatever is
    // left after the longest palindromic subsequence —
    // which is the longest common subsequence of the
    // string and its reverse.
    const n = s.length;
    const rev = s.split("").reverse().join("");
    let prev: number[] = new Array(n + 1).fill(0);
    for (let i = 1; i <= n; i++) {
        const cur: number[] = new Array(n + 1).fill(0);
        for (let j = 1; j <= n; j++) {
            if (s[i - 1] === rev[j - 1]) {
                cur[j] = prev[j - 1] + 1;
            } else {
                cur[j] = Math.max(prev[j], cur[j - 1]);
            }
        }
        prev = cur;
    }
    return n - prev[n];
}
