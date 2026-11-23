// LeetCode 2663. Lexicographically Smallest Beautiful String — Hard
// https://leetcode.com/problems/lexicographically-smallest-beautiful-string/
// Submission 2201867357 — Accepted, Go
//
// My thinking: a string is beautiful
// exactly when no letter repeats its
// neighbour or the one before that, so
// I walk back from the end, lift the
// first letter I can, and fill the rest
// with the smallest letters that keep
// the rule — the first lift that works
// is the smallest larger string.

package main

func smallestBeautifulString(s string, k int) string {
	n := len(s)
	a := make([]int, n)
	for i, c := range s {
		a[i] = int(c - 'a')
	}
	for i := n - 1; i >= 0; i-- {
		for c := a[i] + 1; c < k; c++ {
			if i >= 1 && c == a[i-1] {
				continue
			}
			if i >= 2 && c == a[i-2] {
				continue
			}
			res := append([]int{}, a[:i]...)
			res = append(res, c)
			for j := i + 1; j < n; j++ {
				for d := 0; d < k; d++ {
					if d != res[len(res)-1] && (len(res) < 2 || d != res[len(res)-2]) {
						res = append(res, d)
						break
					}
				}
			}
			out := make([]byte, n)
			for j, v := range res {
				out[j] = byte(v + 'a')
			}
			return string(out)
		}
	}
	return ""
}
