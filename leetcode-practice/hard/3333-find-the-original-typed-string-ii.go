// LeetCode 3333. Find the Original Typed String II — Hard
// https://leetcode.com/problems/find-the-original-typed-string-ii/
// Submission 2202379473 -- Accepted, Go
package main

func possibleStringCount(word string, k int) int {
	// My thinking: split the word into runs of equal letters with lengths
	// c1..cm. The original string chose 1..ci letters from each run, so
	// there are c1 * ... * cm originals in total. I only need to subtract
	// the ones shorter than k: a DP over runs counts, for each length j < k,
	// how many choices sum to exactly j, with prefix sums making each run
	// O(k). If k is at most the number of runs, every original is already
	// long enough and the answer is the total.
	const MOD = 1000000007
	groups := []int{}
	n := len(word)
	for i := 0; i < n; {
		j := i
		for j < n && word[j] == word[i] {
			j++
		}
		groups = append(groups, j-i)
		i = j
	}
	m := len(groups)
	total := 1
	for _, c := range groups {
		total = total * c % MOD
	}
	if k <= m {
		return total
	}
	dp := make([]int, k)
	dp[0] = 1
	for _, c := range groups {
		pref := make([]int, k+1)
		for j := 0; j < k; j++ {
			pref[j+1] = (pref[j] + dp[j]) % MOD
		}
		ndp := make([]int, k)
		for j := 1; j < k; j++ {
			lo := j - c
			if lo < 0 {
				lo = 0
			}
			ndp[j] = (pref[j] - pref[lo] + MOD) % MOD
		}
		dp = ndp
	}
	short := 0
	for _, v := range dp {
		short = (short + v) % MOD
	}
	return (total - short + MOD) % MOD
}
