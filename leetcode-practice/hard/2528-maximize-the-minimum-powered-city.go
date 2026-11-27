// LeetCode 2528. Maximize the Minimum Powered City — Hard
// https://leetcode.com/problems/maximize-the-minimum-powered-city/
// Submission 2201798637 — Accepted, Go
//
// My thinking: the answer only grows
// one way, so I binary-search it — for
// a target I walk the cities left to
// right, and whenever one falls short I
// plant the missing stations as far
// right as they still reach it, so they
// help the most cities ahead.

package main

func maxPower(stations []int, r int, k int) int {
	n := len(stations)
	prefix := make([]int, n+1)
	for i, x := range stations {
		prefix[i+1] = prefix[i] + x
	}
	power := func(i int) int {
		lo := i - r
		if lo < 0 {
			lo = 0
		}
		hi := i + r
		if hi > n-1 {
			hi = n - 1
		}
		return prefix[hi+1] - prefix[lo]
	}
	feasible := func(target int) bool {
		added := make([]int, n+1)
		used := 0
		running := 0
		for i := 0; i < n; i++ {
			running += added[i]
			cur := power(i) + running
			if cur < target {
				need := target - cur
				used += need
				if used > k {
					return false
				}
				pos := i + r
				if pos > n-1 {
					pos = n - 1
				}
				running += need
				if pos+r+1 < n {
					added[pos+r+1] -= need
				}
			}
		}
		return used <= k
	}
	lo, hi := 0, 0
	for _, x := range stations {
		hi += x
	}
	hi += k + 1
	for lo < hi {
		mid := (lo + hi + 1) / 2
		if feasible(mid) {
			lo = mid
		} else {
			hi = mid - 1
		}
	}
	return lo
}
