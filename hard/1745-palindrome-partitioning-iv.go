// LeetCode 1745. Palindrome Partitioning IV — Hard
// https://leetcode.com/problems/palindrome-partitioning-iv/
// Submission 2201138871 — Accepted, Go
//
// My thinking: I mark every palindromic substring
// first, then I just need two cut points where all
// three pieces are marked — the first piece, the
// middle piece, and the last piece.

func checkPartitioning(s string) bool {
    n := len(s)
    isPal := make([][]bool, n)
    for i := range isPal {
        isPal[i] = make([]bool, n)
    }
    for i := n - 1; i >= 0; i-- {
        for j := i; j < n; j++ {
            if s[i] == s[j] && (j-i < 2 || isPal[i+1][j-1]) {
                isPal[i][j] = true
            }
        }
    }
    for i := 0; i < n; i++ {
        for j := i + 1; j < n-1; j++ {
            if isPal[0][i] && isPal[i+1][j] && isPal[j+1][n-1] {
                return true
            }
        }
    }
    return false
}
