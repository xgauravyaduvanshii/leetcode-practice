// LeetCode 3177. Find the Maximum Length of a Good Subsequence II — Hard
// https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-ii/
// Submission 2202061796 — Accepted, Go
//
// My thinking: for each allowed number
// of changes t I keep, per value, the
// longest good subsequence ending in
// that value, plus the best and
// second-best lengths over all values.
// Extending by x either repeats x,
// spends a change on a different best
// value, or continues the same value
// from t-1 — and I update the two bests
// so the next value can pick a different
// one.

func maximumLength(nums []int, k int) int {
    K := k
    f := make([]map[int]int, K+1)
    for i := range f {
        f[i] = make(map[int]int)
    }
    best1Val := make([]int, K+1)
    best1Len := make([]int, K+1)
    best2Len := make([]int, K+1)
    for _, x := range nums {
        for t := K; t >= 0; t-- {
            old := f[t][x]
            cand := old + 1
            if t > 0 {
                prevSame := f[t-1][x]
                if prevSame+1 > cand {
                    cand = prevSame + 1
                }
                b := best1Len[t-1]
                if best1Val[t-1] == x {
                    b = best2Len[t-1]
                }
                if b+1 > cand {
                    cand = b + 1
                }
            }
            if cand > old {
                f[t][x] = cand
                if best1Val[t] == x {
                    best1Len[t] = cand
                } else if cand > best1Len[t] {
                    best2Len[t] = best1Len[t]
                    best1Len[t] = cand
                    best1Val[t] = x
                } else if cand > best2Len[t] {
                    best2Len[t] = cand
                }
            }
        }
    }
    return best1Len[K]
}
