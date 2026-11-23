// LeetCode 2565. Subsequence With the Minimum Score — Hard
// https://leetcode.com/problems/subsequence-with-the-minimum-score/
// Submission 2201822717 — Accepted, Go
//
// My thinking: I keep a prefix of t and
// a suffix of t, and the part I cut out
// is whatever sits between them — I
// learn how far each prefix reaches into
// s and where each suffix must start,
// then slide the cut until the two ends
// just meet.

package main

func minimumScore(s string, t string) int {
	n, m := len(s), len(t)
	const INF = 1 << 30
	// pref[i]: index in s just after matching t[:i]; INF if impossible
	pref := make([]int, m+1)
	for i := range pref {
		pref[i] = INF
	}
	pref[0] = 0
	p := 0
	for i := 0; i < m; i++ {
		for p < n && s[p] != t[i] {
			p++
		}
		if p == n {
			break
		}
		p++
		pref[i+1] = p
	}
	// suff[i]: index in s where the match of t[i:] starts; -1 if impossible
	suff := make([]int, m+1)
	for i := range suff {
		suff[i] = -1
	}
	suff[m] = n
	p = n - 1
	for i := m - 1; i >= 0; i-- {
		for p >= 0 && s[p] != t[i] {
			p--
		}
		if p < 0 {
			break
		}
		suff[i] = p
		p--
	}
	if pref[m] <= n {
		return 0
	}
	ans := m
	r := -1
	for l := 0; l <= m; l++ {
		if pref[l] == INF {
			break
		}
		if r < l-1 {
			r = l - 1
		}
		for r+1 < m && suff[r+1] < pref[l] {
			r++
		}
		if r-l+1 < ans {
			ans = r - l + 1
		}
	}
	return ans
}
