// LeetCode 1994. The Number of Good Subsets — Hard
// https://leetcode.com/problems/the-number-of-good-subsets/
// Submission 2201296027 — Accepted, Go
//
// My thinking: a good subset's product has no
// repeated prime, so I track which primes are
// already used in a mask — square numbers are
// out at once, and the 1s just double the count.

package main

const mod1994 = 1000000007

func numberOfGoodSubsets(nums []int) int {
	primes := []int{2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
	maskOf := func(v int) int {
		m := 0
		for i, p := range primes {
			cnt := 0
			for v%p == 0 {
				v /= p
				cnt++
			}
			if cnt > 1 {
				return -1
			}
			if cnt == 1 {
				m |= 1 << i
			}
		}
		if v > 1 {
			return -1
		}
		return m
	}
	freq := map[int]int{}
	for _, v := range nums {
		freq[v]++
	}
	ones := freq[1]
	dp := make([]int, 1<<10)
	dp[0] = 1
	for v, c := range freq {
		if v == 1 {
			continue
		}
		m := maskOf(v)
		if m == -1 {
			continue
		}
		ndp := make([]int, 1<<10)
		copy(ndp, dp)
		for mask := 0; mask < 1<<10; mask++ {
			if dp[mask] != 0 && mask&m == 0 {
				ndp[mask|m] = (ndp[mask|m] + dp[mask]*c) % mod1994
			}
		}
		dp = ndp
	}
	total := 0
	for _, x := range dp {
		total = (total + x) % mod1994
	}
	total = (total - 1 + mod1994) % mod1994
	pow2 := 1
	for i := 0; i < ones; i++ {
		pow2 = pow2 * 2 % mod1994
	}
	return total * pow2 % mod1994
}
