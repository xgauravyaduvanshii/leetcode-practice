// LeetCode 4027. Elevator Requests III — Hard
// https://leetcode.com/problems/elevator-requests-iii/
// Submission 2203517482 — Accepted, Go
//
// My thinking: with at most 16 requests, try every order
// they can be fulfilled in — a bitmask DP over the set of
// requests done so far. dp[mask][i] is the earliest time
// at which exactly the requests in mask are fulfilled and
// the elevator stands at request i's floor. Going from i
// to a new request j costs the floor distance, and the
// elevator may have to wait at j's floor until j's arrival
// time, so the new time is max(old + |floor_i - floor_j|,
// arrival_j). Starting out, reaching request i costs
// max(|start - floor_i|, arrival_i). Passing through a
// floor on the way to another request never beats visiting
// it in order, so the cheapest order the DP finds is the
// true optimum. The answer is the best dp value over all
// last requests in the full mask.
func minTime(n int, start int, requests [][]int) int {
	m := len(requests)
	floors := make([]int, m)
	arrive := make([]int, m)
	for i, r := range requests {
		floors[i] = r[1]
		arrive[i] = r[0]
	}
	const INF = int(1e18)
	size := 1 << m
	dp := make([][]int, size)
	for mask := range dp {
		dp[mask] = make([]int, m)
		for i := range dp[mask] {
			dp[mask][i] = INF
		}
	}
	for i := 0; i < m; i++ {
		t := start - floors[i]
		if t < 0 {
			t = -t
		}
		if t < arrive[i] {
			t = arrive[i]
		}
		dp[1<<i][i] = t
	}
	for mask := 0; mask < size; mask++ {
		for i := 0; i < m; i++ {
			if mask&(1<<i) == 0 {
				continue
			}
			cur := dp[mask][i]
			if cur == INF {
				continue
			}
			for j := 0; j < m; j++ {
				if mask&(1<<j) != 0 {
					continue
				}
				d := floors[i] - floors[j]
				if d < 0 {
					d = -d
				}
				t := cur + d
				if t < arrive[j] {
					t = arrive[j]
				}
				nm := mask | (1 << j)
				if t < dp[nm][j] {
					dp[nm][j] = t
				}
			}
		}
	}
	ans := INF
	for _, t := range dp[size-1] {
		if t < ans {
			ans = t
		}
	}
	return ans
}
