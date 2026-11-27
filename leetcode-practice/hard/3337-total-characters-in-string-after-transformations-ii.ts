// LeetCode 3337. Total Characters in String After Transformations II — Hard
// https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/
// Submission 2202391271 -- Accepted, TypeScript
function lengthAfterTransformations(s: string, t: number, nums: number[]): number {
    // My thinking: only the counts of each letter matter. One transformation
    // maps letter i to one copy each of the next nums[i] letters, which is
    // a 26x26 transition matrix. I raise that matrix to the t-th power by
    // binary exponentiation and apply it to the initial count vector; the
    // answer is the total count afterwards. A row sum of the powered matrix
    // is the number of descendants of one letter after t transformations.
    // The matrix products use BigInt so the modular multiplications stay
    // exact (plain numbers would lose precision above 2^53).
    const MOD = 1000000007n;
    const n = 26;
    const mat: bigint[][] = Array.from({length: n}, () => new Array(n).fill(0n));
    for (let i = 0; i < n; i++) {
        for (let d = 1; d <= nums[i]; d++) {
            mat[i][(i + d) % n] = (mat[i][(i + d) % n] + 1n) % MOD;
        }
    }
    function matMult(A: bigint[][], B: bigint[][]): bigint[][] {
        const C: bigint[][] = Array.from({length: n}, () => new Array(n).fill(0n));
        for (let i = 0; i < n; i++) {
            for (let k = 0; k < n; k++) {
                const aik = A[i][k];
                if (aik !== 0n) {
                    for (let j = 0; j < n; j++) {
                        C[i][j] = (C[i][j] + aik * B[k][j]) % MOD;
                    }
                }
            }
        }
        return C;
    }
    let power: bigint[][] = Array.from({length: n}, (_, i) =>
        Array.from({length: n}, (_, j) => i === j ? 1n : 0n));
    let base = mat;
    let e = t;
    while (e > 0) {
        if (e & 1) power = matMult(power, base);
        base = matMult(base, base);
        e = Math.floor(e / 2);
    }
    const cnt = new Array(n).fill(0);
    for (const ch of s) cnt[ch.charCodeAt(0) - 97]++;
    let ans = 0n;
    for (let i = 0; i < n; i++) {
        if (cnt[i] !== 0) {
            let rowSum = 0n;
            for (let j = 0; j < n; j++) rowSum = (rowSum + power[i][j]) % MOD;
            ans = (ans + BigInt(cnt[i]) * rowSum) % MOD;
        }
    }
    return Number(ans);
}
