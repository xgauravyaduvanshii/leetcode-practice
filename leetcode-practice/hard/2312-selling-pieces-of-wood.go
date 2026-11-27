// LeetCode 2312. Selling Pieces of Wood — Hard
// https://leetcode.com/problems/selling-pieces-of-wood/
// Submission 2201673499 — Accepted, Go
//
// My thinking: any board is either sold as
// it stands or split once — so I fill a
// table of best prices for every size and
// let each size take the best of selling
// whole or cutting across or down.

package main

func sellingWood(m int, n int, prices [][]int) int64 {
	price := make([][]int64, m+1)
	for i := range price {
		price[i] = make([]int64, n+1)
	}
	for _, p := range prices {
		price[p[0]][p[1]] = int64(p[2])
	}
	dp := make([][]int64, m+1)
	for i := range dp {
		dp[i] = make([]int64, n+1)
	}
	for h := 1; h <= m; h++ {
		for w := 1; w <= n; w++ {
			best := price[h][w]
			for k := 1; k <= w/2; k++ {
				if dp[h][k]+dp[h][w-k] > best {
					best = dp[h][k] + dp[h][w-k]
				}
			}
			for k := 1; k <= h/2; k++ {
				if dp[k][w]+dp[h-k][w] > best {
					best = dp[k][w] + dp[h-k][w]
				}
			}
			dp[h][w] = best
		}
	}
	return dp[m][n]
}
