// LeetCode 2742. Painting the Walls — Hard
// https://leetcode.com/problems/painting-the-walls/
// NOT SUBMITTED — LeetCode's Go judge failed on 23–24 Nov 2026
// ("runtime/cgo: pthread_create failed: Resource temporarily unavailable"),
// 5 attempts in total, so no Run ever became Accepted and the code was
// deliberately not submitted. The code below is the correct knapsack solution
// (same logic as the Accepted Python3 submission 2201878983). Re-submit when
// LeetCode's Go judge recovers.
//
// My thinking: every wall I pay for
// covers itself and buys the free
// painter that many more walls of time,
// so the whole job is a knapsack — I
// pick the cheapest set of paid walls
// whose own count plus their bought
// time covers every wall.

func paintWalls(cost []int, time []int) int {
    n := len(cost)
    const INF = int(1e18)
    dp := make([]int, n+1)
    for i := range dp {
        dp[i] = INF
    }
    dp[0] = 0
    for idx, c := range cost {
        t := time[idx]
        for k := n; k >= 0; k-- {
            if dp[k] == INF {
                continue
            }
            nk := k + 1 + t
            if nk > n {
                nk = n
            }
            if dp[k]+c < dp[nk] {
                dp[nk] = dp[k] + c
            }
        }
    }
    return dp[n]
}
