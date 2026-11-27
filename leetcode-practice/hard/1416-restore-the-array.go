func numberOfArrays(s string, k int) int {
	// My thinking: from each position, try every length
	// up to ten digits — no leading zero, and the number
	// must stay within k — then add the ways from where
	// that number ends.
	const MOD = 1000000007
	n := len(s)
	dp := make([]int, n+1)
	dp[n] = 1
	for i := n - 1; i >= 0; i-- {
		if s[i] == '0' {
			continue
		}
		num := 0
		for j := i; j < n && j < i+10; j++ {
			num = num*10 + int(s[j]-'0')
			if num > k {
				break
			}
			dp[i] = (dp[i] + dp[j+1]) % MOD
		}
	}
	return dp[0]
}
