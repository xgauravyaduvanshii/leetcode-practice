// LeetCode 2400. Number of Ways to Reach a Position After Exactly k Steps — Medium
// https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/
// Submission 2204783119 — Accepted, Go
//
// My thinking: same idea as the Python version — the walk must take
// (k + d) / 2 steps toward the target, so the answer is C(k, right),
// computed here with Pascal's triangle modulo 1e9+7. Impossible when
// the target is farther than k or the parity doesn't match.
func numberOfWays(startPos int, endPos int, k int) int {
    const mod = 1000000007
    d := endPos - startPos
    if d < 0 {
        d = -d
    }
    if d > k || (k-d)%2 == 1 {
        return 0
    }
    right := (k + (endPos - startPos)) / 2
    comb := make([][]int, k+1)
    for i := range comb {
        comb[i] = make([]int, k+1)
        comb[i][0] = 1
        comb[i][i] = 1
        for j := 1; j < i; j++ {
            comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % mod
        }
    }
    return comb[k][right]
}
