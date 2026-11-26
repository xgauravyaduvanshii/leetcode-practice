// LeetCode 131. Palindrome Partitioning — Medium
// https://leetcode.com/problems/palindrome-partitioning/
// Submission 2204032267 — Accepted, Go

// My thinking: backtracking over the string: at each position, try every
// possible end index and keep only the substrings that are palindromes.
// A substring is a palindrome when it reads the same forwards and
// backwards, so check s[start:end+1] against its reverse.
// When the start index reaches the end of the string, the current path
// is one complete partition, so save a copy of it.
// Otherwise, for each palindromic prefix starting at the current
// position, add it to the path, recurse from the next position, then
// remove it again (backtrack) to try the next split.
// Every valid partition is found exactly once, because each recursive
// step fixes the next piece of the partition.
func partition(s string) [][]string {
    var result [][]string
    var path []string
    n := len(s)

    isPalindrome := func(sub string) bool {
        for i, j := 0, len(sub)-1; i < j; i, j = i+1, j-1 {
            if sub[i] != sub[j] {
                return false
            }
        }
        return true
    }

    var backtrack func(start int)
    backtrack = func(start int) {
        if start == n {
            copyPath := make([]string, len(path))
            copy(copyPath, path)
            result = append(result, copyPath)
            return
        }
        for end := start; end < n; end++ {
            sub := s[start : end+1]
            if isPalindrome(sub) {
                path = append(path, sub)
                backtrack(end + 1)
                path = path[:len(path)-1]
            }
        }
    }

    backtrack(0)
    return result
}
