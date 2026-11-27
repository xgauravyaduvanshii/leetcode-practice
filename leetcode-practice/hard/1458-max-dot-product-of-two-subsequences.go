func maxDotProduct(nums1 []int, nums2 []int) int {
	// My thinking: at each pair of positions, either skip
	// one side, start a fresh pair here, or extend the best
	// pair built so far — the biggest of those four wins.
	n, m := len(nums1), len(nums2)
	const NEG = -1 << 60
	dp := make([][]int, n+1)
	for i := range dp {
		dp[i] = make([]int, m+1)
		for j := range dp[i] {
			dp[i][j] = NEG
		}
	}
	for i := 1; i <= n; i++ {
		for j := 1; j <= m; j++ {
			prod := nums1[i-1] * nums2[j-1]
			best := dp[i-1][j]
			if dp[i][j-1] > best {
				best = dp[i][j-1]
			}
			if prod > best {
				best = prod
			}
			if dp[i-1][j-1]+prod > best {
				best = dp[i-1][j-1] + prod
			}
			dp[i][j] = best
		}
	}
	return dp[n][m]
}
