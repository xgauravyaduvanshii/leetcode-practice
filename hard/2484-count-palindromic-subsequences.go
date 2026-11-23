// LeetCode 2484. Count Palindromic Subsequences — Hard
// https://leetcode.com/problems/count-palindromic-subsequences/
// Submission 2201775933 — Accepted, Go
//
// My thinking: a length-5 palindrome reads
// a b c b a, so for each middle digit I
// count how many (a, b) pairs sit to its
// left and how many (b, a) pairs sit to
// its right — with only ten digits there
// are just a hundred pairs to track, and
// I sweep both sides once to learn them.

package main

const mod2484 = 1000000007

func countPalindromes(s string) int {
	n := len(s)
	digits := make([]int, n)
	for i, ch := range s {
		digits[i] = int(ch - '0')
	}
	// suffix pair counts: suf[i][b][a] = number of (b, a) pairs in s[i:]
	suf := make([][10][10]int, n+1)
	cnt := [10]int{}
	for i := n - 1; i >= 0; i-- {
		suf[i] = suf[i+1]
		d := digits[i]
		for a := 0; a < 10; a++ {
			suf[i][d][a] += cnt[a]
		}
		cnt[d]++
	}
	ans := 0
	left := [10][10]int{}
	seen := [10]int{}
	for i := 0; i < n; i++ {
		if i+1 < n {
			right := suf[i+1]
			for a := 0; a < 10; a++ {
				for b := 0; b < 10; b++ {
					ans = (ans + left[a][b]*right[b][a]) % mod2484
				}
			}
		}
		d := digits[i]
		for a := 0; a < 10; a++ {
			left[a][d] += seen[a]
		}
		seen[d]++
	}
	return ans
}
