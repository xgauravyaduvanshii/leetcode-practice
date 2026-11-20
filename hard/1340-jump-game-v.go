import "sort"

func maxJumps(arr []int, d int) int {
	// My thinking: from each spot you can only jump over
	// smaller heights, so the longest walk from a spot is
	// one more than the best walk from anywhere you can
	// reach — work from the lowest spots upward.
	n := len(arr)
	dp := make([]int, n)
	for i := range dp {
		dp[i] = 1
	}
	order := make([]int, n)
	for i := range order {
		order[i] = i
	}
	sort.Slice(order, func(a, b int) bool { return arr[order[a]] < arr[order[b]] })
	for _, i := range order {
		for step := 1; step <= d; step++ {
			j := i + step
			if j >= n || arr[j] >= arr[i] {
				break
			}
			if dp[j]+1 > dp[i] {
				dp[i] = dp[j] + 1
			}
		}
		for step := 1; step <= d; step++ {
			j := i - step
			if j < 0 || arr[j] >= arr[i] {
				break
			}
			if dp[j]+1 > dp[i] {
				dp[i] = dp[j] + 1
			}
		}
	}
	best := 0
	for _, v := range dp {
		if v > best {
			best = v
		}
	}
	return best
}
