// LeetCode 3995. Minimum Cost to Convert String III — Hard
// https://leetcode.com/problems/minimum-cost-to-convert-string-iii/
// Submission 2203501740 — Accepted, Go
//
// My thinking: each position is used by at most one
// rule application, so the string under a rule is
// still the original source there — a rule can only
// help if its pattern matches the source segment and
// its replacement equals the target segment. That
// turns the problem into a shortest path over
// positions: dp[i] is the cheapest cost of converting
// the first i characters. From i we may leave a
// matching character untouched for free, or apply any
// rule whose replacement equals target[i:i+L] and
// whose pattern matches source[i:i+L], paying its
// base cost plus one per wildcard. Grouping the rules
// by (length, replacement) means only the few rules
// that can produce the needed target segment are
// tried.
package main

import "sort"

type ruleEntry struct {
	pat  string
	cost int
}

func minCost(source string, target string, rules [][]string, costs []int) int {
	n := len(source)
	const inf = int(1) << 60
	byLen := make(map[int]map[string][]ruleEntry)
	for i, rule := range rules {
		pat, rep := rule[0], rule[1]
		wild := 0
		for j := 0; j < len(pat); j++ {
			if pat[j] == '*' {
				wild++
			}
		}
		L := len(pat)
		m := byLen[L]
		if m == nil {
			m = make(map[string][]ruleEntry)
			byLen[L] = m
		}
		m[rep] = append(m[rep], ruleEntry{pat, costs[i] + wild})
	}
	lengths := make([]int, 0, len(byLen))
	for L := range byLen {
		lengths = append(lengths, L)
	}
	sort.Ints(lengths)
	dp := make([]int, n+1)
	for i := range dp {
		dp[i] = inf
	}
	dp[0] = 0
	for i := 0; i < n; i++ {
		if dp[i] == inf {
			continue
		}
		if source[i] == target[i] && dp[i] < dp[i+1] {
			dp[i+1] = dp[i]
		}
		for _, L := range lengths {
			if i+L > n {
				continue
			}
			for _, e := range byLen[L][target[i:i+L]] {
				ok := true
				for k := 0; k < L; k++ {
					if e.pat[k] != '*' && e.pat[k] != source[i+k] {
						ok = false
						break
					}
				}
				if ok && dp[i]+e.cost < dp[i+L] {
					dp[i+L] = dp[i] + e.cost
				}
			}
		}
	}
	if dp[n] == inf {
		return -1
	}
	return dp[n]
}
