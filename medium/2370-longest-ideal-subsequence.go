// LeetCode 2370. Longest Ideal Subsequence — Medium
// https://leetcode.com/problems/longest-ideal-subsequence/
// Submission 2204758431 — Accepted, Go
//
// My thinking: same idea as the Python version — dp[c] is the longest
// ideal subsequence ending with letter c; each new letter extends the
// best dp value within k of it, and the answer is the largest dp value.
func longestIdealString(s string, k int) int {
    dp := [26]int{}
    for i := 0; i < len(s); i++ {
        c := int(s[i] - 'a')
        lo := c - k
        if lo < 0 {
            lo = 0
        }
        hi := c + k
        if hi > 25 {
            hi = 25
        }
        best := 0
        for j := lo; j <= hi; j++ {
            if dp[j] > best {
                best = dp[j]
            }
        }
        dp[c] = best + 1
    }
    ans := 0
    for _, v := range dp {
        if v > ans {
            ans = v
        }
    }
    return ans
}
